---
type: protein-evaluation
gene: "NYAP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NYAP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NYAP2 / KIAA1486 |
| 蛋白名称 | Neuronal tyrosine-phosphorylated phosphoinositide-3-kinase adapter 2 |
| 蛋白大小 | 653 aa / 70.5 kDa |
| UniProt ID | Q9P242 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Microtubules, Primary cilium, Cytosol; 额外: Nucleoplasm, Cyto; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 653 aa / 70.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026722, IPR029353, IPR039482; Pfam: PF15452, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules, Primary cilium, Cytosol; 额外: Nucleoplasm, Cytokinetic bridge, Mitotic spindle, Basal body | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1486 |

**关键文献**:
1. Integrative RNA-seq and ATAC-seq analyses of phosphodiesterase 6 mutation-induced retinitis pigmentosa.. *International ophthalmology*. PMID: 35147831
2. Genomic Exploration of Selection Signatures Linked to Reproductive Traits in Locally Adapted Indicine, Taurine and Crossbred Cattle of India.. *Reproduction in domestic animals = Zuchthygiene*. PMID: 40631534
3. Decoding the DNA of Anatolian water buffalo by genome-wide discoveries for body size and ultrasound carcass traits.. *BMC veterinary research*. PMID: 41310724
4. Identification of growth trait related genes in a Yorkshire purebred pig population by genome-wide association studies.. *Asian-Australasian journal of animal sciences*. PMID: 27809465
5. The PTN-PTPRZ signal activates the AFAP1L2-dependent PI3K-AKT pathway for oligodendrocyte differentiation: Targeted inactivation of PTPRZ activity in mice.. *Glia*. PMID: 30667096

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.2 |
| 高置信度残基 (pLDDT>90) 占比 | 7.5% |
| 置信残基 (pLDDT 70-90) 占比 | 9.0% |
| 中等置信 (pLDDT 50-70) 占比 | 29.4% |
| 低置信 (pLDDT<50) 占比 | 54.1% |
| 有序区域 (pLDDT>70) 占比 | 16.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=54.2），有序残基占 16.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026722, IPR029353, IPR039482; Pfam: PF15452, PF15439 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WASF1 | 0.660 | 0.301 | — |
| MORN4 | 0.503 | 0.503 | — |
| NYAP1 | 0.486 | 0.000 | — |
| PIK3R1 | 0.441 | 0.441 | — |
| MYO16 | 0.430 | 0.000 | — |
| FAM110D | 0.424 | 0.000 | — |
| CYFIP1 | 0.423 | 0.328 | — |
| NCKAP1 | 0.421 | 0.301 | — |
| AGFG1 | 0.410 | 0.361 | — |
| PRR7 | 0.407 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FYN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| AGFG1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| MORN4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| Dlc1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| PIK3R1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cyfip1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| SEMG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HDAC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SUFU | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 9
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.2 + PDB: 无 | pLDDT=54.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Microtubules, Primary cilium, Cytosol; 额外: Nucleop | 待确认 |
| PPI | STRING + IntAct | 10 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NYAP2 — Neuronal tyrosine-phosphorylated phosphoinositide-3-kinase adapter 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小653 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P242
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144460-NYAP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NYAP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P242
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
