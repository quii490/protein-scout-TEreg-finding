---
type: protein-evaluation
gene: "TANK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TANK — REJECTED (研究热度过高 (PubMed strict=2945，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TANK |
| 蛋白名称 | TANK (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | TANK |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoli; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2945 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **53/180** | |
| **归一化总分** | | | **29.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli | Supported |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2945 |
| PubMed broad count | 22323 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. TBK1 and IKKε prevent TNF-induced cell death by RIPK1 phosphorylation.. *Nature cell biology*. PMID: 30420664
2. The STING phase-separator suppresses innate immune signalling.. *Nature cell biology*. PMID: 33833429
3. Induction of antiviral interferon-stimulated genes by neuronal STING promotes the resolution of pain in mice.. *The Journal of clinical investigation*. PMID: 38690737
4. Epoxyeicosatrienoic Acids Prevent Cardiac Dysfunction in Viral Myocarditis via Interferon Type I Signaling.. *Circulation research*. PMID: 37681352
5. PRMT1 (protein arginine methyltransferase 1) is essential for neuromuscular junction and mitochondrial homeostasis via mitophagy regulation.. *Autophagy*. PMID: 40851194

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
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000376505.2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| EBI-26730181 | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| Traf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Traf1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| ZC3H12A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TBK1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| HSPA1L | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| HSPA5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| HSPA8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Cytosol; 额外: Nucleoli | 待确认 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐ (REJECTED)

**核心优势**:
1. TANK — TANK (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 2945 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2945 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/TANK
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136560-TANK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TANK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/TANK
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000136560-TANK/subcellular

![](https://images.proteinatlas.org/10345/1144_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10345/1144_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10345/954_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10345/954_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10345/956_C9_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/10345/956_C9_7_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92844 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR041641;IPR039669;IPR024581; |
| Pfam | PF12845; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000136560-TANK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APBA3 | Intact, Biogrid | true |
| CEP63 | Intact, Biogrid | true |
| IKBKE | Intact, Biogrid | true |
| IKBKG | Intact, Biogrid | true |
| PLK1 | Intact, Biogrid | true |
| TBK1 | Intact, Biogrid | true |
| TRAF1 | Intact, Biogrid, Bioplex | true |
| TRAF2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
