---
type: protein-evaluation
gene: "ESPNL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ESPNL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ESPNL |
| 蛋白名称 | Espin-like protein |
| 蛋白大小 | 1005 aa / 108.1 kDa |
| UniProt ID | Q6ZVH7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm, Nuclear bodies, Vesicles; UniProt: Cell projection, stereocilium |
| 蛋白大小 | 8/10 | ×1 | 8 | 1005 aa / 108.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR052420; Pfam: PF12796, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Nuclear bodies, Vesicles | Approved |
| UniProt | Cell projection, stereocilium | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- stereocilium tip (GO:0032426)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genome-wide association studies identify susceptibility loci for epithelial ovarian cancer in east Asian women.. *Gynecologic oncology*. PMID: 30898391
2. A Whole Methylome Study of Ethanol Exposure in Brain and Blood: An Exploration of the Utility of Peripheral Blood as Proxy Tissue for Brain in Alcohol Methylation Studies.. *Alcoholism, clinical and experimental research*. PMID: 30320886
3. Identification of stage-specific markers during differentiation of hair cells from mouse inner ear stem cells or progenitor cells in vitro.. *The international journal of biochemistry & cell biology*. PMID: 25582750
4. Identification of immune-related gene signature predicting survival in the tumor microenvironment of lung adenocarcinoma.. *Immunogenetics*. PMID: 33188484
5. Loss of Baiap2l2 destabilizes the transducing stereocilia of cochlear hair cells and leads to deafness.. *The Journal of physiology*. PMID: 33151556

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.7 |
| 高置信度残基 (pLDDT>90) 占比 | 31.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.8% |
| 中等置信 (pLDDT 50-70) 占比 | 12.0% |
| 低置信 (pLDDT<50) 占比 | 37.3% |
| 有序区域 (pLDDT>70) 占比 | 50.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.7），有序残基占 50.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR052420; Pfam: PF12796, PF13637 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYO3B | 0.962 | 0.412 | — |
| MYO3A | 0.958 | 0.412 | — |
| EPS8L2 | 0.912 | 0.045 | — |
| MYO15A | 0.910 | 0.126 | — |
| WHRN | 0.908 | 0.099 | — |
| TWF2 | 0.888 | 0.100 | — |
| EPS8 | 0.885 | 0.045 | — |
| ESPN | 0.834 | 0.000 | — |
| GSN | 0.828 | 0.042 | — |
| MPP1 | 0.811 | 0.098 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PFDN5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LDLRAP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SERTAD2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.7 + PDB: 无 | pLDDT=64.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, stereocilium / Cytosol; 额外: Nucleoplasm, Nuclear bodies, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

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
1. ESPNL — Espin-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1005 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZVH7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144488-ESPNL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ESPNL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZVH7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
