---
type: protein-evaluation
gene: "KEAP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## KEAP1 — REJECTED (研究热度过高 (PubMed strict=5554，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KEAP1 |
| 蛋白名称 | KEAP1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | KEAP1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoplasm, Centriolar satellite; 额外: Cytosol; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=5554 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **60.5/180** | |
| **归一化总分** | | | **33.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centriolar satellite; 额外: Cytosol | Supported |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5554 |
| PubMed broad count | 8831 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Nrf2/Keap1/ARE signaling: Towards specific regulation.. *Life sciences*. PMID: 34732330
2. Signal amplification in the KEAP1-NRF2-ARE antioxidant response pathway.. *Redox biology*. PMID: 35792437
3. The Keap1-Nrf2 System: A Mediator between Oxidative Stress and Aging.. *Oxidative medicine and cellular longevity*. PMID: 34012501
4. Gene Copy Deletion of STK11, KEAP1, and SMARCA4: Clinicopathologic Features and Association With the Outcomes of Immunotherapy With or Without Chemotherapy in Nonsquamous NSCLC.. *Journal of thoracic oncology : official publication of the International Association for the Study of Lung Cancer*. PMID: 39864548
5. Tumor suppressor KEAP1 promotes HSPA9 degradation, controlling mitochondrial biogenesis in breast cancer.. *Cell reports*. PMID: 39003742

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.999 | 0.999 | — |
| RBX1 | 0.999 | 0.820 | — |
| SQSTM1 | 0.999 | 0.995 | — |
| NFE2L2 | 0.999 | 0.999 | — |
| NEIL2 | 0.999 | 0.301 | — |
| PGAM5 | 0.998 | 0.832 | — |
| IKBKB | 0.997 | 0.833 | — |
| PALB2 | 0.996 | 0.847 | — |
| PTMA | 0.993 | 0.903 | — |
| DPP3 | 0.992 | 0.841 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Delta | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| pug | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mcm3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| SmB | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ctr9 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG14540 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ikbkb | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| ETF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RELA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| TSC22D4 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm, Centriolar satellite; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. KEAP1 — KEAP1 (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 5554 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 5554 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/KEAP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000079999-KEAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KEAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/KEAP1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000079999-KEAP1/subcellular

![](https://images.proteinatlas.org/5558/68_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/5558/68_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/5558/69_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/5558/69_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/5558/91_B4_11_red_green.jpg)
![](https://images.proteinatlas.org/5558/91_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
