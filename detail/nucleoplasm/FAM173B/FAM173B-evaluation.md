---
type: protein-evaluation
gene: "FAM173B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM173B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM173B / FAM173B |
| 蛋白名称 | ATP synthase subunit C lysine N-methyltransferase |
| 蛋白大小 | 233 aa / 26.1 kDa |
| UniProt ID | Q6P4H8 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM173B/IF_images/HeLa_1.jpg|HeLa]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM173B/IF_images/SiHa_1.jpg|SiHa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Mitochondrion membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 233 aa / 26.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026170, IPR029063 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Mitochondrion membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- mitochondrial crista (GO:0030061)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM173B |

**关键文献**:
1. Expression of mitochondrial TSPO and FAM173B is associated with inflammation and symptoms in patients with painful knee osteoarthritis.. *Rheumatology (Oxford, England)*. PMID: 33067627
2. Lysine methylation by the mitochondrial methyltransferase FAM173B optimizes the function of mitochondrial ATP synthase.. *The Journal of biological chemistry*. PMID: 30530489
3. Human FAM173A is a mitochondrial lysine-specific methyltransferase that targets adenine nucleotide translocase and affects mitochondrial respiration.. *The Journal of biological chemistry*. PMID: 31213526
4. Identification of FAM173B as a protein methyltransferase promoting chronic pain.. *PLoS biology*. PMID: 29444090
5. Genome-wide association study meta-analysis of chronic widespread pain: evidence for involvement of the 5p15.2 region.. *Annals of the rheumatic diseases*. PMID: 22956598

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.9 |
| 高置信度残基 (pLDDT>90) 占比 | 62.7% |
| 置信残基 (pLDDT 70-90) 占比 | 13.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 16.7% |
| 有序区域 (pLDDT>70) 占比 | 76.4% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM173B/FAM173B-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=81.9，有序区 76.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026170, IPR029063 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CMBL | 0.884 | 0.000 | — |
| CCT5 | 0.699 | 0.062 | — |
| EEF1AKMT1 | 0.534 | 0.000 | — |
| METTL18 | 0.522 | 0.053 | — |
| EEF1AKMT2 | 0.501 | 0.000 | — |
| VCPKMT | 0.495 | 0.000 | — |
| METTL22 | 0.494 | 0.000 | — |
| METTL21A | 0.492 | 0.000 | — |
| TRMT112 | 0.487 | 0.400 | — |
| TULP4 | 0.472 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATPSCKMT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MEOX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 2
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.9 + PDB: 无 | pLDDT=81.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion membrane / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 14 + 2 interactions | 数据充分 |

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
1. FAM173B — ATP synthase subunit C lysine N-methyltransferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小233 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P4H8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150756-ATPSCKMT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM173B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P4H8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM173B/FAM173B-PAE.png]]




