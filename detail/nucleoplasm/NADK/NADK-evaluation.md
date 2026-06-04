---
type: protein-evaluation
gene: "NADK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NADK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NADK |
| 蛋白名称 | NAD kinase |
| 蛋白大小 | 446 aa / 49.2 kDa |
| UniProt ID | O95544 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 446 aa / 49.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=80 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.4; PDB: 3PFN, 8KGC, 9CR3, 9CR4, 9CRA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017438, IPR017437, IPR016064, IPR002504; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 80 |
| PubMed broad count | 158 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular properties and regulation of NAD(+) kinase (NADK).. *Redox biology*. PMID: 36512915
2. NUAK1-Mediated Phosphorylation of NADK Mitigates ROS Accumulation to Promote Osimertinib Resistance in Non-Small Cell Lung Carcinoma.. *Cancer research*. PMID: 39159134
3. NAD+ kinase--a review.. *The International journal of biochemistry*. PMID: 2987053
4. NMRK2-YAP-NADK axis preserves redox protection against myocardial ischemia/reperfusion injury.. *Redox biology*. PMID: 41762891
5. Cryo-EM structure and regulation of human NAD kinase.. *Science advances*. PMID: 39854463

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.4 |
| 高置信度残基 (pLDDT>90) 占比 | 63.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 20.0% |
| 有序区域 (pLDDT>70) 占比 | 74.9% |
| 可用 PDB 条目 | 3PFN, 8KGC, 9CR3, 9CR4, 9CRA |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3PFN, 8KGC, 9CR3, 9CR4, 9CRA）+ AlphaFold极高置信度预测（pLDDT=80.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017438, IPR017437, IPR016064, IPR002504; Pfam: PF01513, PF20143 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H6PD | 0.919 | 0.000 | — |
| G6PD | 0.917 | 0.000 | — |
| IDH1 | 0.886 | 0.098 | — |
| IDH2 | 0.881 | 0.098 | — |
| RNASEH1 | 0.825 | 0.000 | — |
| NT5E | 0.810 | 0.000 | — |
| GPD1 | 0.805 | 0.000 | — |
| GPD1L | 0.805 | 0.000 | — |
| NADK2 | 0.792 | 0.000 | — |
| FDFT1 | 0.723 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-2260114 | psi-mi:"MI:0363"(inferred by author) | imex:IM-11644|pubmed:19965468 |
| Nadk1a | psi-mi:"MI:0397"(two hybrid array) | pubmed:unassigned1513|imex:IM- |
| nadk-1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19123269 |
| Nadk1b | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| POS5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:27107014|imex:IM-24995 |
| YEF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:27107014|imex:IM-24995 |
| NADK3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32612234|imex:IM-27834 |
| NUDT18 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LNX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GLRX3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.4 + PDB: 3PFN, 8KGC, 9CR3, 9CR4, 9CRA | pLDDT=80.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NADK — NAD kinase，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小446 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 80 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95544
- Protein Atlas: https://www.proteinatlas.org/ENSG00000008130-NADK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NADK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95544
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
