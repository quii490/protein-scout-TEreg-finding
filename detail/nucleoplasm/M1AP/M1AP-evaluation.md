---
type: protein-evaluation
gene: "M1AP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## M1AP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | M1AP / C2orf65, SPATA37 |
| 蛋白名称 | Meiosis 1 arrest protein |
| 蛋白大小 | 530 aa / 59.4 kDa |
| UniProt ID | Q8TC57 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nucleoli; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 530 aa / 59.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033587 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoli | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C2orf65, SPATA37 |

**关键文献**:
1. In vivo versus in silico assessment of potentially pathogenic missense variants in human reproductive genes.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37459509
2. Genotype-specific differences in infertile men due to loss-of-function variants in M1AP or ZZS genes.. *EMBO molecular medicine*. PMID: 40374915
3. Genetic Variants of CLPP and M1AP Are Associated With Risk of Non-Small Cell Lung Cancer.. *Frontiers in oncology*. PMID: 34604049
4. Structural analysis of M1AP variants associated with severely impaired spermatogenesis causing male infertility.. *PeerJ*. PMID: 35341049
5. CRISPR screening identifies M1AP as a new MYC regulator with a promoter-reporter system.. *PeerJ*. PMID: 32411526

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.4 |
| 高置信度残基 (pLDDT>90) 占比 | 42.5% |
| 置信残基 (pLDDT 70-90) 占比 | 20.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.8% |
| 低置信 (pLDDT<50) 占比 | 25.8% |
| 有序区域 (pLDDT>70) 占比 | 63.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=73.4，有序区 63.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033587 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AMDHD2 | 0.710 | 0.000 | — |
| AMDHD2-2 | 0.709 | 0.000 | — |
| H6PD | 0.613 | 0.000 | — |
| FBXO47 | 0.596 | 0.000 | — |
| STAG3 | 0.584 | 0.000 | — |
| STPG2 | 0.582 | 0.000 | — |
| MEIOC | 0.565 | 0.000 | — |
| MEI1 | 0.558 | 0.000 | — |
| SHOC1 | 0.545 | 0.000 | — |
| GNPDA2 | 0.524 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=73.4 + PDB: 无 | pLDDT=73.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Mitochondria; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. M1AP — Meiosis 1 arrest protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小530 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TC57
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159374-M1AP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=M1AP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TC57
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
