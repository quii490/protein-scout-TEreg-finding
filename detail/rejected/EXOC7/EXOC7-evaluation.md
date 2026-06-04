---
type: protein-evaluation
gene: "EXOC7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EXOC7 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOC7 / EXO70, KIAA1067 |
| 蛋白名称 | Exocyst complex component 7 |
| 蛋白大小 | 735 aa / 83.4 kDa |
| UniProt ID | Q9UPT5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; 额外: Vesicles, Plasma membrane; UniProt: Cytoplasm, cytosol; Cell membrane; Midbody, Midbody ring |
| 蛋白大小 | 10/10 | ×1 | 10 | 735 aa / 83.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016159, IPR004140, IPR046364; Pfam: PF03081, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Vesicles, Plasma membrane | Approved |
| UniProt | Cytoplasm, cytosol; Cell membrane; Midbody, Midbody ring | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- cytosol (GO:0005829)
- exocyst (GO:0000145)
- Flemming body (GO:0090543)
- growth cone membrane (GO:0032584)
- membrane (GO:0016020)
- microtubule organizing center (GO:0005815)
- midbody (GO:0030496)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 84 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EXO70, KIAA1067 |

**关键文献**:
1. A fine balance between Prpf19 and Exoc7 in achieving degradation of aggregated protein and suppression of cell death in spinocerebellar ataxia type 3.. *Cell death & disease*. PMID: 33542212
2. Regulation of human cerebral cortical development by EXOC7 and EXOC8, components of the exocyst complex, and roles in neural progenitor cell proliferation and survival.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 32103185
3. Identification of Alternative Splicing Events Associated with Paratuberculosis in Dairy Cattle Using Multi-Tissue RNA Sequencing Data.. *Genes*. PMID: 35328051
4. Inducible Exoc7/Exo70 knockout reveals a critical role of the exocyst in insulin-regulated GLUT4 exocytosis.. *The Journal of biological chemistry*. PMID: 31740584
5. A novel nonsense variant in EXOC8 underlies a neurodevelopmental disorder.. *Neurogenetics*. PMID: 35460391

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.6 |
| 高置信度残基 (pLDDT>90) 占比 | 70.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 16.3% |
| 有序区域 (pLDDT>70) 占比 | 80.6% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=82.6，有序区 80.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016159, IPR004140, IPR046364; Pfam: PF03081, PF20669 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RHOQ | 0.999 | 0.446 | — |
| EXOC4 | 0.999 | 0.993 | — |
| EXOC1 | 0.999 | 0.979 | — |
| EXOC2 | 0.999 | 0.989 | — |
| EXOC6 | 0.999 | 0.977 | — |
| EXOC8 | 0.999 | 0.991 | — |
| EXOC5 | 0.999 | 0.975 | — |
| EXOC3 | 0.999 | 0.928 | — |
| EXOC6B | 0.994 | 0.976 | — |
| CDC42 | 0.968 | 0.250 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USHBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KXD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| IFT20 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RTN4IP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PRPF19 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HGS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZC3H14 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| AKTIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.6 + PDB: 无 | pLDDT=82.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Cell membrane; Midbody, Midbod / Cytosol; 额外: Vesicles, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EXOC7 — Exocyst complex component 7，非常新颖，仅有少数基础研究。
2. 蛋白大小735 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPT5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182473-EXOC7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOC7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPT5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
