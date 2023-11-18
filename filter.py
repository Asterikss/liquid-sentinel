# from transformers import pipeline
#
# oracle = pipeline(model="deepset/roberta-base-squad2")
# oracle(question="Is this ?", context="PDF\nTabela 2. Oprocentowanie środków pieniężnych na rachunkach dla małych i średnich przedsiębiorstw rachunki wycofane z oferty")

l = [('Komunikat PKO Banku Polskiego (Zawiera m.in wartości oprocentowania przeterminowanego)', 'https://www.pkobp.pl/api/default/a8a3eeb5-9672-47de-810f-72f2cc48164a.pdf'),
('PDF\nZasady i terminy kapitalizacji odsetek od środków pieniężnych w walutach wymienialnych gromadzonych na rachunkach bankowych oraz od kredytów w walutach wymienialnych udzielanych przez PKO Bank Polski Spółkę Akcyjną', 'https://www.pkobp.pl/api/public/889b8dc5-f7ba-4889-aae4-5f5ebcffa4de.pdf'),
('PDF\nTabela 1. Oprocentowanie na rachunkach oszczędnościowych i rachunkach terminowych lokat oszczędnościowych osób fizycznych w walutach wymienialnych w ofercie', 'https://www.pkobp.pl/api/public/092b2cb6-40ee-41dc-b90b-6515b656da47.pdf'),
('PDF\nTabela 1. Oprocentowanie na rachunkach oszczędnościowych i rachunkach terminowych lokat oszczędnościowych osób fizycznych w walutach wymienialnych wycofane z oferty', 'https://www.pkobp.pl/api/public/3f2eac2b-8c80-49e4-974c-25698505edbe.pdf'),
('PDF\nTabela 2. Oprocentowanie środków pieniężnych na rachunkach dla małych i średnich przedsiębiorstw rachunki w ofercie', 'https://www.pkobp.pl/api/public/8ef10057-d4d6-4601-96ed-8b5c19687d4b.pdf'),
('PDF\nTabela 2. Oprocentowanie środków pieniężnych na rachunkach dla małych i średnich przedsiębiorstw rachunki wycofane z oferty', 'https://www.pkobp.pl/api/public/551bcb1a-464c-493a-a947-ab38f4910413.pdf')]

bad_words: list[str] = ["wycofanych", "wycofany", "wycofane", "nieaktulany", "nieaktualnych"]

# for i, desc in enumerate(l):
#     for bd in bad_words:
#         if bd in desc:
#             del desc
updated_list = [desc for desc in l if not any(bad_word in desc[0] for bad_word in bad_words)]

print(updated_list)
print(len(l), len(updated_list))
            
