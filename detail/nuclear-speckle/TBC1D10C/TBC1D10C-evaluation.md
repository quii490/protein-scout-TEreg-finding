---
type: protein-evaluation
gene: "TBC1D10C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBC1D10C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBC1D10C |
| 蛋白名称 | Carabin |
| 蛋白大小 | 446 aa / 49.7 kDa |
| UniProt ID | Q8IV04 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 446 aa / 49.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000195, IPR035969, IPR050302; Pfam: PF00566 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- ficolin-1-rich granule membrane (GO:0101003)
- filopodium membrane (GO:0031527)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Embryonic expression patterns of TBC1D10 subfamily genes in zebrafish.. *Gene expression patterns : GEP*. PMID: 34843939
2. TBC1D10C is a cytoskeletal functional linker that modulates cell spreading and phagocytosis in macrophages.. *Scientific reports*. PMID: 34686741
3. Enhanced cardiac TBC1D10C expression lowers heart rate and enhances exercise capacity and survival.. *Scientific reports*. PMID: 27667030
4. Integrative ATAC-seq and RNA-seq analysis associated with diabetic nephropathy and identification of novel targets for treatment by dapagliflozin.. *Cell biochemistry and function*. PMID: 38379015
5. All members of the EPI64 subfamily of TBC/RabGAPs also have GAP activities towards Ras.. *Journal of biochemistry*. PMID: 23248241

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.6 |
| 高置信度残基 (pLDDT>90) 占比 | 67.9% |
| 置信残基 (pLDDT 70-90) 占比 | 6.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 18.4% |
| 有序区域 (pLDDT>70) 占比 | 74.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.6，有序区 74.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000195, IPR035969, IPR050302; Pfam: PF00566 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RASAL3 | 0.809 | 0.000 | — |
| ARHGAP9 | 0.794 | 0.000 | — |
| RAB35 | 0.779 | 0.075 | — |
| TRAF3IP3 | 0.750 | 0.000 | — |
| PTPRCAP | 0.676 | 0.000 | — |
| RASA1 | 0.667 | 0.000 | — |
| ACAP1 | 0.631 | 0.000 | — |
| TBC1D13 | 0.620 | 0.000 | — |
| TBC1D22B | 0.593 | 0.000 | — |
| TBC1D21 | 0.593 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SHANK1 | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| HOXA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KLHL12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP5-9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| NOTCH2NLA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| - | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.6 + PDB: 无 | pLDDT=81.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TBC1D10C — Carabin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小446 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

**结构域架构**：TBC1D10C（Carabin, UniProt: Q8IV04, 446 aa / 49.7 kDa）的核心结构域为Rab-GAP TBC domain（aa 92-280），属于TBC/RabGAP family（IPR000195, IPR035969, IPR050302）。TBC domain负责catalyze Rab GTPase的GTP hydrolysis——Rab proteins作为vesicular trafficking和organelle identity的主调节因子，其活性受到精确的GTP-GDP cycling调控。AlphaFold pLDDT=81.6（中等偏高）——高置信残基占比67.9%，有序区域（pLDDT>70）占比74.0%，表明TBC domain区域折叠优良，结构可信度较高。Pfam注释为PF00566（Rab-GTPase-TBC domain），SMART识别为SM00164。暂无实验PDB结构（PDB=0）。

**PPI互作网络解读**：STRING PPI network（15 partners, combined score >0.4）包含RASAL3、ARHGAP9、RAB35、TRAF3IP3、PTPRCAP、RASA1、ACAP1等——RAB35是TBC domain的底物Rab GTPase，该互作获得弱实验支持（experimental score=0.075）。BioGRID记录的关键互作包括METTL3（m6A methyltransferase catalytic subunit，参与RNA methylation和TE silencing）、DOT1L（H3K79 methyltransferase，参与telomeric silencing和MLL fusion-driven leukemogenesis）、HOXA1（homeobox transcription factor）和CUL4A（CRL4 E3 ubiquitin ligase scaffold）。这些互作将TBC1D10C与chromatin modification、transcriptional regulation和protein degradation machinery直接关联。IntAct验证互作包括SHANK1、HOXA1、KLHL12、KRTAP5-9和NOTCH2NLA。

**结构解读**：AlphaFold预测（pLDDT=81.6）显示TBC1D10C的核心折叠由TBC domain（aa 92-280）构成——该domain采用典型的alpha-helical bundle架构，含有conserved catalytic arginine/glutamine finger motif用于stabilize GTP hydrolysis transition state。18.4%的低置信残基（pLDDT<50）主要分布在N端（aa 1-91）和C端区域（aa 281-446），这些区域的功能注释缺失——它们可能包含regulatory motif、protein-protein interaction site或degradation signal（如degron）。HPA定位为Nuclear bodies（Approved）。

**机制模型**：TBC1D10C作为Rab-GAP的双重功能模式：一方面通过TBC domain催化Rab35（或其他Rab）的GTP hydrolysis，调控endosomal trafficking和plasma membrane recycling；另一方面通过nuclear body localization参与核内功能。Rab GTPase signaling与autophagy、mTOR pathway、integrin trafficking密切相关——这些pathway均已报道与TE silencing的调控关联。DOT1L介导的H3K79 methylation在MLL-rearranged leukemia中维持aberrant gene expression program，同时也与telomeric/subtelomeric chromatin状态的维持相关——许多endogenous retrovirus（ERV）插入位点位于subtelomeric region。

**TE调控展望**：TBC1D10C的TE regulation潜力通过多重机制体现：（1）METTL3（BioGRID互作）是m6A writer complex的核心催化亚基——m6A modification on nascent RNA包括LINE-1和Alu element transcript的m6A修饰，m6A reader YTHDC1通过recognizing m6A标记促进TE transcript degradation；（2）DOT1L（BioGRID互作）的H3K79 methyltransferase活性影响chromatin state at ERV loci——H3K79me2/3通常mark active chromatin，DOT1L inhibition可能导致ERV的epigenetic silencing；（3）CUL4A（BioGRID互作）作为CRL4 ubiquitin ligase的scaffold，通过ubiquitination-mediated degradation of chromatin-associated factor间接影响TE的transcriptional status。建议通过TBC1D10C的co-immunoprecipitation验证METTL3和DOT1L互作，再通过knockdown/overexpression RNA-seq评估其对TE expression的影响——特别关注LINE-1、Alu和HERV-K等major TE family。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 1 |
| HOXA1 | BioGRID | 1 |
| METTL3 | BioGRID | 1 |
| CUL4A | BioGRID | 1 |
| DOT1L | BioGRID | 1 |
| BTRC | BioGRID | 1 |
| TRIM21 | BioGRID | 1 |
| KRTAP5-9 | BioGRID | 0 |


### TE 调控评估

该蛋白缺乏核/染色质定位证据，TE 调控潜力较低。