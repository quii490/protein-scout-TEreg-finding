---
type: protein-evaluation
gene: "SSTR2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, rejected]
status: rejected
---

## SSTR2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SSTR2 |
| 蛋白大小 | 369 aa / 41.3 kDa |
| UniProt ID | P30874 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 369 aa |
| 新颖性 | 0/10 | ×5 | 0.0 | PubMed=499 |
| 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=81.3; PDB=17 |
| 调控结构域 | 4/10 | ×2 | 8.0 | GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; Somatstn_rcpt |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=24 |
| **加权总分** | | | **91/180** | |
| **归一化总分** | | | **50.8/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Supported)
- PubMed strict=499 broad=1540
- AF pLDDT=81.3 PDB=17
- InterPro: GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; Somatstn_rcpt
- Pfam: 7tm_1
- PPI degree=24 ChIP: None
39116368: Structure and Function of Somatostatin and Its Receptors in Endocrinology. | 32644756: Octreotide Scan. | 23136682: (68)Ga-1,4,7,10-Tetraazacyclododecane-1,4,7,10-tetraacetic acid-p-Cl-Phe-cyclo(D

### 深度机制分析

**结构域架构**：SSTR2（369 aa, 41.3 kDa, P30874, Somatostatin receptor type 2, SSTR2/SS2R）是G protein-coupled receptor（GPCR）family 1 member——为典型的class A rhodopsin-like GPCR。结构域：7个transmembrane α-helices（TM1-TM7, TM bundle）——形成7TM barrel fold——胞外侧三个extracellular loops（ECL1-ECL3）和N-terminal tail——胞内侧三个intracellular loops（ICL1-ICL3）和C-terminal tail。细胞外ligand-binding pocket由TM3/TM4/TM5/TM6/TM7的extracellular half和ECL2组成——somastatin（SST-14, cyclic tetradecapeptide, Ala-Gly-c[Cys-Lys-Asn-Phe-Phe-Trp-Lys-Thr-Phe-Thr-Ser-Cys]-OH）中的Phe-Trp-Lys-Thr pharmacophore motif插入TM barrel约15A深的orthosteric binding pocket——Phe7/W8/Lys9 of SST-14与TM2 Asp71, TM3 Asn102, TM7 Tyr302形成氢键和π-π stacking。GPCR_Rhodpsn（InterPro: IPR000276/Pfam PF00001）和GPCR_Rhodpsn_7TM（InterPro: IPR017452）为classical GPCR fold signature。Somatostatin receptor family（InterPro: IPR002074）的conserved motif为TM3的ERY（Glu-Arg-Tyr）DRY motif和TM6的NPxxY motif——DRY为Gi/o coupling determinant——Arg residue（Arg131 in SSTR2）的ionic lock与TM6 Glu形成intramolecular salt bridge——维持inactive conformation——agonist binding breaks this ionic lock→TM6 outward movement→Gαi C-terminal α5-helix binding pocket opening →GDP/GTP exchange on Gαi。

**PPI互作网络解读**：STRING PPI network显示SSTR2的mutual Gαi-coupled network：GNAI1/GNAI2/GNAI3——SSTR2优先couple to Gαi1/Gαi2/Gαi3——激活→Gαi-GTP dissociation from Gβγ——Gαi-GTP抑制adenylyl cyclase（AC）→降低cAMP production→reduced PKA activity。Gβγ dimer直接激活GIRK potassium channels（Kir3.x）→K+ efflux→membrane hyperpolarization——或抑制voltage-gated calcium channels（Cav2.2, N-type）→reduced Ca2+ influx→抑制neurotransmitter release。SSTR2 coupling优先性：SST-14 IC50=0.2-1.3 nM, SST-28 IC50=0.2-1.6 nM。

**结构解读**：PDB=17个实验结构——包括SSTR2-Gi complex（cryo-EM 3.2-4.0 A）——清晰展示SSTR2的agonist-bound active state和antagonist/inverse agonist-bound inactive state。AlphaFold pLDDT=81.3——7TM bundle为高置信度（pLDDT>85）——N-terminal tail和C-terminal tail pLDDT<50（IDR区，提供phosphorylation-dependent regulatory sites）。IL3 loop连接TM5-TM6为largest intracellular loop——G protein coupling interface——C-terminal tail含6个Ser/Thr phosphorylation sites（putative GRK2/GRK3 sites）——phosphorylated C-tail招募β-arrestin 1/2（ARRB1/ARRB2）——启动G protein-independent signaling（MAP kinase ERK1/2, via β-arrestin scaffold）和receptor internalization（clathrin-mediated endocytosis）。

**机制模型**：（1）Neuroendocrine signaling——SSTR2在hypothalamus、pituitary、pancreatic δ-cells和GI tract enteroendocrine cells中高度表达——在pituitary somatotroph cell中SST通过SSTR2自分泌/旁分泌方式抑制GH release——通过Gαi-AC-cAMP-PKA axis和Gi/o-Gβγ-Cav channel axis双重抑制胞吐。Octreotide（SMS 201-995, synthetic SST-14 analog, D-Phe-c[Cys-Phe-D-Trp-Lys-Thr-Cys]-Thr-ol, IC50=0.4 nM）为SSTR2-preferring agonist——用于acromegaly、neuroendocrine tumors的clinical management。（2）Nucleoplasm localization——HPA标注Cytosol; Nucleoplasm（Supported）——GPCR的nuclear pool已成为新兴信号领域——nuclear GPCR可直接在nuclear membrane或nucleoplasm中感知ligand——调控CREB, AP-1, NFκB等transcription factor的activity——而不通过canonical G protein signaling的cytoplasmic propagation. Nuclear SSTR2可能通过Gi-AC-cAMP轴调控nuclear PKA activity——PKA phosphorylates nuclear CREB at Ser133→CBP/p300 recruitment→CREB-dependent transcription——间接调控含有CREB response element（CRE: 5'-TGACGTCA-3'）的TE LTR promoter。

**TE调控展望**：SSTR2通过nuclear GPCR signaling间接参与TE调控。GPCR nuclear pool中Gi-AC-cAMP-PKA-CREB signaling axis是最well-established机制——CREB response element（CRE, TGACGTCA）与LTR promoter的enhancer element（如HERV-K LTR-5HS CRE-interacting enhancer, 含CRE-like motif）存在显著motif homology——核SSTR2 activation可能通过PKA-CREB axis调控CREB-dependent TE transcription。Somatostatin/SSTR2 axis是否在nucleoplasm中directly modulate TE loci的CREB occupancy——需要通过ChIP-seq验证SSTR2 activation-dependent CREB enrichment at retrotransposon LTR CRE sites。SSTR2的rejected状态（PubMed=499, novelty=0/10）基于经典neuroendocrine research热度而非TE function relevance——若focus仅限于SSTR2在TE regulation中的novel role，其可重新评估。

### 4. 总体评价
**50.8/100** | **rejected**
Nuclear protein
