---
type: protein-evaluation
gene: "DEGS2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DEGS2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DEGS2 / C14orf66 |
| 蛋白名称 | Sphingolipid delta(4)-desaturase/C4-monooxygenase DES2 |
| 蛋白大小 | 323 aa / 37.2 kDa |
| UniProt ID | Q6QHC5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nucleoli; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 323 aa / 37.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=96.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011388, IPR005804, IPR013866; Pfam: PF00487, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 115 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf66 |

**关键文献**:
1. Delta 4-desaturase sphingolipid 2 enhances prostate cancer stem-like traits through phytoceramide-mediated PI3K-AKT signaling pathway.. *Carcinogenesis*. PMID: 40380873
2. Effects of Th1/Th17 and Th2 cytokines on lipid metabolism in differentiated keratinocytes.. *Frontiers in physiology*. PMID: 40046180
3. DEGS2 polymorphism associated with cognition in schizophrenia is associated with gene expression in brain.. *Translational psychiatry*. PMID: 25871975
4. Breast Cancer Bone Metastasis: Novel Prognostic Biomarkers Identified.. *Phenomics (Cham, Switzerland)*. PMID: 41001431
5. Multi-omics integration identifies NK cell dysregulation and a five-gene diagnostic signature in major depressive disorder.. *Frontiers in immunology*. PMID: 41601671

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.3 |
| 高置信度残基 (pLDDT>90) 占比 | 95.4% |
| 置信残基 (pLDDT 70-90) 占比 | 2.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 97.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.3，有序区 97.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011388, IPR005804, IPR013866; Pfam: PF00487, PF08557 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CERS4 | 0.972 | 0.071 | — |
| CERS6 | 0.968 | 0.071 | — |
| CERS5 | 0.967 | 0.071 | — |
| KDSR | 0.967 | 0.000 | — |
| CERS2 | 0.964 | 0.071 | — |
| CERS3 | 0.963 | 0.071 | — |
| UGCG | 0.961 | 0.000 | — |
| ACER1 | 0.956 | 0.000 | — |
| ACER2 | 0.954 | 0.000 | — |
| CERK | 0.953 | 0.067 | — |

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
| 三维结构 | AlphaFold pLDDT=96.3 + PDB: 无 | pLDDT=96.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nucleoplasm, Nucleoli | 一致 |
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
1. DEGS2 — Sphingolipid delta(4)-desaturase/C4-monooxygenase DES2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小323 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6QHC5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168350-DEGS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DEGS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6QHC5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
