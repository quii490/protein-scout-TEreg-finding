---
type: protein-evaluation
gene: "TMOD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TMOD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TMOD2 / NTMOD |
| 蛋白名称 | Tropomodulin-2 |
| 蛋白大小 | 351 aa / 39.6 kDa |
| UniProt ID | Q9NZR1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center; 额外: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 10/10 | ×1 | 10 | 351 aa / 39.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR032675, IPR004934; Pfam: PF03250 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoskeleton (GO:0005856)
- myofibril (GO:0030016)
- striated muscle thin filament (GO:0005865)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NTMOD |

**关键文献**:
1. Multiplex cerebrospinal fluid proteomics identifies biomarkers for diagnosis and prediction of Alzheimer's disease.. *Nature human behaviour*. PMID: 38987357
2. TMOD2 and DOCK4 as Novel Gut Microbiota-Associated Biomarkers for Colorectal Adenoma: Integrated Transcriptomic Analysis and Therapeutic Target Identification.. *Mediators of inflammation*. PMID: 41378121
3. Deciphering the central role of TMOD2 in colorectal cancer progression and metastasis.. *British journal of cancer*. PMID: 40962847
4. Tmod2 Is a Regulator of Cocaine Responses through Control of Striatal and Cortical Excitability and Drug-Induced Plasticity.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 38508714
5. Hexavalent chromium causes centrosome amplification by inhibiting the binding between TMOD2 and NPM2.. *Toxicology letters*. PMID: 36963620

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.8 |
| 高置信度残基 (pLDDT>90) 占比 | 49.3% |
| 置信残基 (pLDDT 70-90) 占比 | 30.8% |
| 中等置信 (pLDDT 50-70) 占比 | 17.7% |
| 低置信 (pLDDT<50) 占比 | 2.3% |
| 有序区域 (pLDDT>70) 占比 | 80.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=83.8，有序区 80.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032675, IPR004934; Pfam: PF03250 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NEB | 0.967 | 0.000 | — |
| ADD1 | 0.955 | 0.000 | — |
| ADD2 | 0.944 | 0.000 | — |
| ADD3 | 0.937 | 0.000 | — |
| GSN | 0.911 | 0.811 | — |
| DMTN | 0.894 | 0.000 | — |
| CARMIL2 | 0.881 | 0.000 | — |
| EPB41 | 0.822 | 0.054 | — |
| SCIN | 0.819 | 0.620 | — |
| CAPZA2 | 0.794 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| SNCA | psi-mi:"MI:0096"(pull down) | pubmed:18614564|imex:IM-19211 |
| PARK7 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| MYDGF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ARHGEF17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| VAV1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| PLEKHG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| PLEKHG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ARHGEF11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.8 + PDB: 无 | pLDDT=83.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / Nucleoli fibrillar center; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TMOD2 — Tropomodulin-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小351 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZR1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128872-TMOD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMOD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZR1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
