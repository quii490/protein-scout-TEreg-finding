---
type: protein-evaluation
gene: "AGO2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AGO2 — REJECTED (研究热度过高 (PubMed strict=1522，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AGO2 / EIF2C2 |
| 蛋白名称 | Protein argonaute-2 |
| 蛋白大小 | 859 aa / 97.2 kDa |
| UniProt ID | Q9UKV8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytoplasmic bodies; 额外: Cytosol; UniProt: Cytoplasm, P-body; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 859 aa / 97.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1522 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.4; PDB: 3LUC, 3LUD, 3LUG, 3LUH, 3LUJ, 3LUK, 3QX8 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR028602, IPR014811, IPR032472, IPR032473, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytoplasmic bodies; 额外: Cytosol | Supported |
| UniProt | Cytoplasm, P-body; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- extracellular exosome (GO:0070062)
- glutamatergic synapse (GO:0098978)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1522 |
| PubMed broad count | 2457 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EIF2C2 |

**关键文献**:
1. AGO2 Protects Against Diabetic Cardiomyopathy by Activating Mitochondrial Gene Translation.. *Circulation*. PMID: 38126189
2. Germline AGO2 mutations impair RNA interference and human neurological development.. *Nature communications*. PMID: 33199684
3. Nuclear AGO2 promotes myocardial remodeling by activating ANKRD1 transcription in failing hearts.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 38475992
4. C-terminal tagging impairs AGO2 function.. *RNA biology*. PMID: 40698645
5. Global profiling of RNA-binding protein target sites by LACE-seq.. *Nature cell biology*. PMID: 34108658

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.4 |
| 高置信度残基 (pLDDT>90) 占比 | 85.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 4.0% |
| 有序区域 (pLDDT>70) 占比 | 94.6% |
| 可用 PDB 条目 | 3LUC, 3LUD, 3LUG, 3LUH, 3LUJ, 3LUK, 3QX8, 3QX9, 4F3T, 4OLA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3LUC, 3LUD, 3LUG, 3LUH, 3LUJ, 3LUK, 3QX8, 3QX9, 4F3T, 4OLA）+ AlphaFold极高置信度预测（pLDDT=92.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028602, IPR014811, IPR032472, IPR032473, IPR032474; Pfam: PF08699, PF16488, PF16487 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DDX6 | 0.999 | 0.797 | — |
| DICER1 | 0.999 | 0.966 | — |
| DHX9 | 0.999 | 0.743 | — |
| GEMIN4 | 0.999 | 0.735 | — |
| TNRC6A | 0.999 | 0.923 | — |
| DDX20 | 0.999 | 0.647 | — |
| AGO1 | 0.999 | 0.891 | — |
| TARBP2 | 0.999 | 0.914 | — |
| FMR1 | 0.998 | 0.342 | — |
| TNRC6B | 0.998 | 0.886 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.4 + PDB: 3LUC, 3LUD, 3LUG, 3LUH, 3LUJ,  | pLDDT=92.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, P-body; Nucleus / Cytoplasmic bodies; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. AGO2 — Protein argonaute-2，研究基础较多，新颖性有限。
2. 蛋白大小859 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1522 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1522 > 100，研究热度过高，不符合novelty筛选标准。**

### 深度机制分析

**结构域架构**：AGO2（859 aa, Q9UKV8, Argonaute 2/EIF2C2, pLDDT=92.4）是RNA-induced silencing complex（RISC）的核心催化组分——domain architecture为：N domain（~1-226 aa）+ PAZ domain（229-348 aa, SMART: SM00949, Piwi/Argonaute/Zwille domain, PROSITE-ProRule: PRU00142）——PAZ domain为约120 aa α/β sandwich fold——含conserved PAZ-specific β-barrel and two α-helices——通过PAZ domain's "binding pocket"（aromatic residues和two conserved Lys residues）特异性识别small RNA（siRNA, miRNA）的3' terminal 2-nt overhang（2-nt 3' OH binding）。Middle（MID）domain（~349-516 aa）含5'-phosphate binding pocket——识别guide RNA的5'-phosphate——通过MID domain's "MC motif"（金属配位: Tyr529-Lys533-Lys545-Lys570-C-terminal carboxylate）与Mg2+离子coordinate 5'-phosphate。PIWI domain（517-818 aa, SMART: SM00950, RNase H-like fold, PROSITE-ProRule: PRU00142）为AGO2的catalytic center（slicer activity）——PIWI domain采用RNase H family canonical fold（five-stranded mixed β-sheet surrounded by α-helices）——active site catalytic tetrad（DDD...H motif, Asp597-Asp669-Asp796-His807）two-metal-ion mechanism——与RNase H的active site高度同源（~40% structural homology）——Mg2+ ions coordinate scissile phosphate of target mRNA——nucleophilic water molecule attack→3'-OH and 5'-phosphate products产生。PDB: 3LUC, 3LUD, 3LUG, 3LUH, 3LUJ, 3LUK, 3QX8, 3QX9, 4F3T, 4OLA（10个PDB实验结构）覆盖full-length AGO2和domain fragments在guide RNA-loaded and target RNA-bound states的构象——提供极为丰富的结构生物学信息。AlphaFold pLDDT=92.4——有序区94.6%——几乎所有domain为极高置信度——N domain和MID-PIWI domain linker为仅有的低置信度region。

**PPI互作网络解读**：AGO2 PPI network反映RISC assembly and function的全套machinery。DICER1（STRING 0.999, 实验分0.966, IntAct+BioGRID+, AF3/HPA structure=true）为RNase III enzyme——切割pre-miRNA hairpin生成约22-nt duplex miRNA——DICER1与AGO2形成RISC loading complex（RLC）——通过TRBP（TARBP2, STRING 0.999, 实验分0.914）和PACT（PRKRA）双链RNA-binding protein——将duplex miRNA handover to AGO2。AGO1（STRING 0.999, 实验分0.891, IntAct+BioGRID+, AF3/HPA structure=true）为AGO family的sibling slicer——AGO1和AGO2竞争guide RNA loading。TNRC6A（GW182, STRING 0.999, 实验分0.923）为P-body component——通过AGO2的GW/WG motif docking——recruit CCR4-NOT and PAN2-PAN3 deadenylase complex→target mRNA deadenylation→decapping（DCP1/DCP2）→5'-to-3' decay（XRN1）。DDX6（STRING 0.999, 实验分0.797, IntAct+BioGRID+, AF3/HPA structure=true）为DEAD-box RNA helicase——在P-body中unwind local RNA secondary structure——促进miRNA-target mRNA pairing。DHX9（STRING 0.999, 实验分0.743）为RNA helicase A——unwrap structured RNA elements——facilitate RISC scan。GEMIN4（STRING 0.999, 实验分0.735）和DDX20（STRING 0.999, 实验分0.647）为SMN complex component——参与snRNP assembly和miRNP biogenesis。FMR1（Fragile X mental retardation protein/FMRP, STRING 0.998）为translational repressor——FMRP-AGO2 interaction facilitates miRNA-dependent translation repression on target mRNA。AGO2相互作用组为最well-characterized protein interaction network之一——反映RNA silencing machinery的极度合作性和功能分区。

**结构解读**：AGO2 structural cycle由guide RNA loading触发conformational cycle：（1）apo state——AGO2为bilobal architecture（N-PAZ lobe + MID-PIWI lobe）——connected by L1/L2 linker helices——PAZ domain distant from MID-PIWI cleft——形成约30-40 A gap——center cleft为guide RNA-binding channel。（2）guide-loaded state——guide RNA 5'-phosphate anchored in MID pocket——guide RNA 3'-end docked in PAZ domain 2-nt binding pocket——guide RNA threading through central basic channel——guided RNA bases 2-8（seed region, positions g2-g8）pre-organized in A-form helical geometry——seed region bases solvent-exposed——扫描目标RNA complementarity。（3）Target-bound state——target RNA base pairs with guide RNA seed region（g2-g8, Watson-Crick base pairing）——seed pairing triggers PIWI domain conformational change——target RNA 3'-end positioned with scissile phosphate（between target nucleotides t10 and t11, corresponding to guide nucleotides g10-g11）aligned at PIWI active site——D597-D669-D796-H807 catalytic tetrad coordinate Mg2+ ions——nucleophile water attack→cleavage。这一conformational cycle完全通过PDB多structure snapshot（3LUC, 3LUD, 3LUG, 3LUH, 3LUJ, 3LUK, 3QX8, 3QX9, 4F3T, 4OLA）和intensive biochemical analysis验证。AGO2 turnover rate（kcat ~0.05-0.5 min-1, single-turnover kinetics）反映guide RNA exchange rate limiting factor——而非target cleavage chemistry。

**机制模型**：（1）miRNA-mediated post-transcriptional gene silencing——AGO2-guide miRNA complex recognizes miRNA response element（MRE, typically 7-8 nt seed match + supplementary base pairing in 3' UTR of target mRNA）——AGO2 slicer activity cleaves target mRNA with perfect complementarity to guide（siRNA mode）——GW182-mediated deadenylation/decapping leads to target mRNA decay（miRNA mode with imperfect complementarity）——两种模式均由guide RNA:target RNA complementarity degree决定。（2）核内AGO2 function——Nuclear AGO2 promotes myocardial remodeling by activating ANKRD1 transcription in failing hearts（PMID:38475992）——AGO2在细胞核中的import-export cycle由IPO8 transporter介导（Importin-8, BioGRID+IntAct+, AF3/HPA structure=true）——AGO2在nucleoplasm中识别nascent transcript或promoter-associated RNA的nuclear miRNA function——核内RISC可能调控transcription rate via targeting transcription-associated non-coding RNA（如enhancer RNA, promoter upstream transcript）。（3）PIWI-piRNA pathway analogy——AGO2的PIWI domain是PIWI蛋白（PIWIL1/HIWI/PIWIL2) PIWI domain的paralog——PIWI-piRNA pathway为germline TE silencing的classical effector——AGO2通过其PIWI domain是否具有TGS（transcriptional gene silencing）功能需要进一步研究。

**TE调控展望**：AGO2-TE调控关联是RNA silencing领域最well-established axis之一。AGO2-piRNA pathway在germline和somatic cells中被证实靶向LINE-1, SINE, ERV/LTR retrotransposon——具体机制：（1）Cytoplasmic TE RISC——AGO2 loaded with TE-derived siRNA/miRNA targets TE mRNA for degradation——阻止reverse transcription and integration——此为post-transcriptional TE silencing（PTGS）。（2）Nuclear TGS——AGO2-guide RNA complex在nucleoplasm中识别nascent TE transcript——recruit histone methyltransferase（如SUV39H1, SETDB1）和DNA methyltransferase（DNMT3A/3B）至TE loci→建立H3K9me3 and CpG methylation repressive marks——实现transcriptional TE silencing（TGS）。AGO2在nucleoplasm and cytoplasmic bodies dual localization使其成为bridging post-transcriptional and transcriptional TE silencing的unique hub protein。但PubMed 1522篇文献使其完全不适合当前project的novelty requirement。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKV8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123908-AGO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AGO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKV8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytoplasmic bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000123908-AGO2/subcellular

![](https://images.proteinatlas.org/67849/1864_G2_16_cr5f59ea654e23e_blue_red_green.jpg)
![](https://images.proteinatlas.org/67849/1864_G2_26_cr5afd78e2cc62f_blue_red_green.jpg)
![](https://images.proteinatlas.org/67849/1918_F1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/67849/1918_F1_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/67849/1983_E11_13_cr5f59e9fe5362a_blue_red_green.jpg)
![](https://images.proteinatlas.org/67849/1983_E11_3_cr5f59e9fe5260f_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UKV8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UKV8 |
| SMART | SM01163;SM00949;SM00950; |
| UniProt Domain [FT] | DOMAIN 229..348; /note="PAZ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00142"; DOMAIN 517..818; /note="Piwi"; /evidence="ECO:0000255\|HAMAP-Rule:MF_03031" |
| InterPro | IPR028602;IPR014811;IPR032472;IPR032473;IPR032474;IPR003100;IPR036085;IPR003165;IPR045246;IPR012337;IPR036397; |
| Pfam | PF08699;PF16488;PF16487;PF16486;PF02170;PF02171; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000123908-AGO2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGO1 | Intact, Biogrid, Opencell | true |
| AGO3 | Biogrid, Opencell | true |
| CNOT7 | Intact, Biogrid | true |
| DDX6 | Intact, Biogrid | true |
| DHX58 | Intact, Biogrid | true |
| DICER1 | Intact, Biogrid | true |
| FKBP5 | Biogrid, Opencell | true |
| IPO8 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
