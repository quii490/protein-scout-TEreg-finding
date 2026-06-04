---
type: protein-evaluation
gene: "SULT1E1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SULT1E1 — REJECTED (研究热度过高 (PubMed strict=173，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SULT1E1 / STE |
| 蛋白名称 | Sulfotransferase 1E1 |
| 蛋白大小 | 294 aa / 35.1 kDa |
| UniProt ID | P49888 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane, Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 294 aa / 35.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=173 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.2; PDB: 1G3M, 1HY3, 4JVL, 4JVM, 4JVN |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR000863; Pfam: PF00685 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Cytosol | Uncertain |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 173 |
| PubMed broad count | 329 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: STE |

**关键文献**:
1. Single-cell analysis reveals insights into epithelial abnormalities in ovarian endometriosis.. *Cell reports*. PMID: 38412094
2. Metformin inhibits testosterone-induced endoplasmic reticulum stress in ovarian granulosa cells via inactivation of p38 MAPK.. *Human reproduction (Oxford, England)*. PMID: 32372097
3. Estrogen Sulfotransferase (SULT1E1): Its Molecular Regulation, Polymorphisms, and Clinical Perspectives.. *Journal of personalized medicine*. PMID: 33799763
4. Overexpression of SULT1E1 alleviates salt-processed Psoraleae Fructus-induced cholestatic liver damage.. *Chinese herbal medicines*. PMID: 40256713
5. Estrogen sulfotransferase SULT1E1 expression correlates with progression and prognosis of lung adenocarcinoma.. *Scientific reports*. PMID: 39762281

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.2 |
| 高置信度残基 (pLDDT>90) 占比 | 95.2% |
| 置信残基 (pLDDT 70-90) 占比 | 3.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 98.9% |
| 可用 PDB 条目 | 1G3M, 1HY3, 4JVL, 4JVM, 4JVN |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1G3M, 1HY3, 4JVL, 4JVM, 4JVN）+ AlphaFold极高置信度预测（pLDDT=97.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR000863; Pfam: PF00685 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TERT | 0.996 | 0.000 | — |
| HSD17B1 | 0.962 | 0.000 | — |
| UGT1A6 | 0.959 | 0.000 | — |
| HSD17B2 | 0.959 | 0.000 | — |
| CYP19A1 | 0.959 | 0.000 | — |
| UGT1A10 | 0.958 | 0.000 | — |
| UGT1A4 | 0.958 | 0.000 | — |
| UGT1A8 | 0.957 | 0.000 | — |
| UGT1A1 | 0.956 | 0.000 | — |
| UGT1A7 | 0.955 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BMPR2 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| SULT2B1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ENOX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TP53 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EEF1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SETDB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| COPS6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RBM48 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.2 + PDB: 1G3M, 1HY3, 4JVL, 4JVM, 4JVN | pLDDT=97.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nuclear membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SULT1E1 — Sulfotransferase 1E1，研究基础较多，新颖性有限。
2. 蛋白大小294 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 173 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 173 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49888
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109193-SULT1E1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SULT1E1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49888
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
