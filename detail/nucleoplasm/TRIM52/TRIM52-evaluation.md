---
type: protein-evaluation
gene: "TRIM52"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRIM52 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIM52 / RNF102 |
| 蛋白名称 | E3 ubiquitin-protein ligase TRIM52 |
| 蛋白大小 | 297 aa / 34.7 kDa |
| UniProt ID | Q96A61 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Intermediate filaments; UniProt: Cytoplasm; Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 297 aa / 34.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050143, IPR000315, IPR001841, IPR013083, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Intermediate filaments | Approved |
| UniProt | Cytoplasm; Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF102 |

**关键文献**:
1. Identification of a novel fusion gene, TRIM52-RACK1, in oral squamous cell carcinoma.. *Molecular and cellular probes*. PMID: 32251686
2. Human tripartite motif protein 52 is required for cell context-dependent proliferation.. *Oncotarget*. PMID: 29568378
3. Tripartite Motif Containing 52 Positively Regulates NF-κB Signaling by Promoting IκBα Ubiquitination in Lipopolysaccharide-Treated Microglial Cell Activation.. *Medical science monitor : international medical journal of experimental and clinical research*. PMID: 33122622
4. TRIM52: A nuclear TRIM protein that positively regulates the nuclear factor-kappa B signaling pathway.. *Molecular immunology*. PMID: 28073078
5. Tripartite motif protein 52 (TRIM52) promoted fibrosis in LX-2 cells through PPM1A-mediated Smad2/3 pathway.. *Cell biology international*. PMID: 31329338

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.8 |
| 高置信度残基 (pLDDT>90) 占比 | 24.2% |
| 置信残基 (pLDDT 70-90) 占比 | 25.3% |
| 中等置信 (pLDDT 50-70) 占比 | 16.5% |
| 低置信 (pLDDT<50) 占比 | 34.0% |
| 有序区域 (pLDDT>70) 占比 | 49.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.8），有序残基占 49.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050143, IPR000315, IPR001841, IPR013083, IPR017907; Pfam: PF00643, PF15227 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPM1A | 0.698 | 0.512 | — |
| TRIM14 | 0.619 | 0.067 | — |
| TRAT1 | 0.604 | 0.000 | — |
| ZNF789 | 0.549 | 0.065 | — |
| RPL31 | 0.542 | 0.507 | — |
| RPSA | 0.533 | 0.507 | — |
| RPS16 | 0.525 | 0.507 | — |
| RPL4 | 0.521 | 0.507 | — |
| RPL30 | 0.520 | 0.507 | — |
| RPLP0 | 0.520 | 0.507 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| tktA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| gcvPA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TRIM41 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| RNF114 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| RNF126 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| UBE2V1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBA1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBE2N | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| MEIOC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KRBA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.8 + PDB: 无 | pLDDT=67.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytosol; Nucleus / Nucleoli; 额外: Intermediate filaments | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TRIM52 — E3 ubiquitin-protein ligase TRIM52，非常新颖，仅有少数基础研究。
2. 蛋白大小297 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96A61
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183718-TRIM52/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM52
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96A61
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000183718-TRIM52/subcellular

![](https://images.proteinatlas.org/54565/867_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/54565/867_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/54565/870_B1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/54565/870_B1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/54565/872_B1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/54565/872_B1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96A61-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96A61 |
| SMART | SM00336;SM00184; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050143;IPR000315;IPR001841;IPR013083;IPR017907; |
| Pfam | PF00643;PF15227; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183718-TRIM52/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TRIM41 | Intact, Biogrid | true |
| NEDD4 | Biogrid | false |
| PPM1A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
