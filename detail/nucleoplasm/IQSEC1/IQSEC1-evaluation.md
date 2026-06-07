---
type: protein-evaluation
gene: "IQSEC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IQSEC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IQSEC1 / ARFGEP100, BRAG2, KIAA0763 |
| 蛋白名称 | IQ motif and SEC7 domain-containing protein 1 |
| 蛋白大小 | 963 aa / 108.3 kDa |
| UniProt ID | Q6DN90 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Vesicles, Centrosome; UniProt: Cytoplasm; Nucleus; Postsynaptic density; Cytoplasmic vesicl |
| 蛋白大小 | 8/10 | ×1 | 8 | 963 aa / 108.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.5; PDB: 3QWM, 4C0A, 5NLV, 5NLY, 6FNE, 7VMB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033742, IPR011993, IPR001849, IPR023394, IPR000 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Vesicles, Centrosome | Supported |
| UniProt | Cytoplasm; Nucleus; Postsynaptic density; Cytoplasmic vesicle, secretory vesicle, synaptic vesicle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- postsynaptic density (GO:0014069)
- synaptic vesicle (GO:0008021)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 76 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARFGEP100, BRAG2, KIAA0763 |

**关键文献**:
1. Genetic associations between gene polymorphisms on 3p25 and oral squamous cell carcinoma.. *Oral diseases*. PMID: 36680374
2. Calcium-stimulated disassembly of focal adhesions mediated by an ORP3/IQSec1 complex.. *eLife*. PMID: 32234213
3. The Identification of Proteolytic Substrates of Calpain-5 with N-Terminomics.. *International journal of molecular sciences*. PMID: 40650235
4. The small GTPase Arf6 is dysregulated in a mouse model for fragile X syndrome.. *Journal of neurochemistry*. PMID: 33125726
5. Contribution of gene polymorphisms on 3p25 to salivary gland carcinoma, ameloblastoma, and odontogenic keratocyst in the Chinese Han population.. *Oral surgery, oral medicine, oral pathology and oral radiology*. PMID: 37495273

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.5 |
| 高置信度残基 (pLDDT>90) 占比 | 33.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 51.2% |
| 有序区域 (pLDDT>70) 占比 | 43.3% |
| 可用 PDB 条目 | 3QWM, 4C0A, 5NLV, 5NLY, 6FNE, 7VMB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.5），有序残基占 43.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033742, IPR011993, IPR001849, IPR023394, IPR000904; Pfam: PF16453, PF01369 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| Irak1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| IRAK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| IRF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| MCM7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23764002|imex:IM-20916 |
| MAGI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Cnksr2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Syngap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.5 + PDB: 3QWM, 4C0A, 5NLV, 5NLY, 6FNE,  | pLDDT=62.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Postsynaptic density; Cytoplas / Cytosol; 额外: Nucleoplasm, Vesicles, Centrosome | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. IQSEC1 — IQ motif and SEC7 domain-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小963 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6DN90
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144711-IQSEC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IQSEC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6DN90
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000144711-IQSEC1/subcellular

![](https://images.proteinatlas.org/69864/1949_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/69864/1949_H11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/69864/2162_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/69864/2162_D11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/69864/2181_C6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/69864/2181_C6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6DN90-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6DN90 |
| SMART | SM00233;SM00222; |
| UniProt Domain [FT] | DOMAIN 134..163; /note="IQ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00116"; DOMAIN 517..710; /note="SEC7"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00189"; DOMAIN 774..866; /note="PH" |
| InterPro | IPR033742;IPR011993;IPR001849;IPR023394;IPR000904;IPR035999; |
| Pfam | PF16453;PF01369; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144711-IQSEC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTL6B | Bioplex | false |
| AGO2 | Biogrid | false |
| ALS2 | Intact | false |
| ARF6 | Biogrid | false |
| BCL2L12 | Bioplex | false |
| BSND | Bioplex | false |
| C6orf141 | Bioplex | false |
| CACNG7 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
