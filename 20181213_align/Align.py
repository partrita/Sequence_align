# import argparse
import glob
from Bio import SeqIO, pairwise2

# Argparse variables
# parser = argparse.ArgumentParser(
#     description='python script for basic sequencing results')
# parser.add_argument(
#     '-d', '--DNA', help='Fasta file of template DNA',
#      type=str, required=True)
# parser.add_argument('-i', '--input', help='Input file', required=True)
# parser.add_argument('-o', '--output', help='Output file', required=True)
# args = parser.parse_args()
# querys = args.input
# subject = args.DNA
# output = args.output

# glob variable
output = 'Algin_result.seq'
querys = glob.glob('*.seq')
subject = glob.glob('Template_*.*')[0]  # 1st template dna only

# Read template DNA
template_ = SeqIO.read(subject, 'fasta')
template_protein = template_.seq.translate()


def align(query, f):
    for seq_record in SeqIO.parse(query, "fasta"):
        print('#### DNA alignments : {} ####'.format(seq_record.id))
        f.write('#### DNA alignments : {} ####\n'.format(seq_record.id))
        alignments = pairwise2.align.localms(
            seq_record.seq, template_.seq, 2, -3, -2, -2)
        print(pairwise2.format_alignment(*alignments[0]))
        f.write(pairwise2.format_alignment(*alignments[0]))
        f.write('\n' * 4)  # add blank line
        print('#### Protein alignments : {} ####'.format(seq_record.id))
        f.write(
            '#### Protein alignments : {} ####\n'.format(seq_record.id))
        # f.write('\n') # add blank line
        # stop codon = *, all frame shift
        forward_1 = seq_record.seq[0::].translate()
        forward_2 = seq_record.seq[1::].translate()
        forward_3 = seq_record.seq[2::].translate()
        reverse_1 = seq_record.seq[:0:-1].translate()  # reverse frame
        reverse_2 = seq_record.seq[:1:-1].translate()
        reverse_3 = seq_record.seq[:2:-1].translate()
        # make list for loop
        protein_seq = [forward_1, forward_2, forward_3,
        reverse_1, reverse_2, reverse_3]
        # alginments
        for i in protein_seq:
            # print frame name?
            alignments = pairwise2.align.localms(
                i, template_protein, 2, -3, -2, -2)
            # print 1st alignments
            # print(pairwise2.format_alignment(*alignments[0]))
            f.write(pairwise2.format_alignment(*alignments[0]))
            # f.write('\n')
        f.write('\n' * 4)  # add blank line


def main():
    '''
    python script for basic sequencing results
    '''

    # simple file write
    with open(output, 'w') as f:
        # f.write('#### Life is short, use python. \n')
        # Simple FASTA parsing
        for query in querys:
            align(query, f)


if __name__ == "__main__":
    main()
