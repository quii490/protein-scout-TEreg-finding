---
type: protein-evaluation
gene: "CALCOCO2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CALCOCO2 — REJECTED (研究热度过高 (PubMed strict=131，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CALCOCO2 / NDP52 |
| 蛋白名称 | Calcium-binding and coiled-coil domain-containing protein 2 |
| 蛋白大小 | 446 aa / 52.3 kDa |
| UniProt ID | Q13137 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Vesicles; UniProt: Cytoplasm, perinuclear region; Cytoplasm, cytoskeleton; Cyto |
| 蛋白大小 | 10/10 | ×1 | 10 | 446 aa / 52.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=131 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.2; PDB: 2MXP, 3VVV, 3VVW, 4GXL, 4HAN, 4XKL, 5AAQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR041641, IPR041611, IPR051002; Pfam: PF17751 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Vesicles | Supported |
| UniProt | Cytoplasm, perinuclear region; Cytoplasm, cytoskeleton; Cytoplasmic vesicle, autophagosome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- autophagosome (GO:0005776)
- autophagosome membrane (GO:0000421)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 131 |
| PubMed broad count | 278 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NDP52 |

**关键文献**:
1. . **. PMID: 35435793
2. . **. PMID: 36622894
3. . **. PMID: 36692217
4. . **. PMID: 35468037
5. . **. PMID: 33906557

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 54.3% |
| 置信残基 (pLDDT 70-90) 占比 | 20.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 17.9% |
| 有序区域 (pLDDT>70) 占比 | 74.9% |
| 可用 PDB 条目 | 2MXP, 3VVV, 3VVW, 4GXL, 4HAN, 4XKL, 5AAQ, 5Z7A, 5Z7L, 7EAA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2MXP, 3VVV, 3VVW, 4GXL, 4HAN, 4XKL, 5AAQ, 5Z7A, 5Z7L, 7EAA）+ AlphaFold极高置信度预测（pLDDT=80.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041641, IPR041611, IPR051002; Pfam: PF17751 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RB1CC1 | 0.999 | 0.933 | — |
| MAP1LC3C | 0.999 | 0.889 | — |
| LGALS8 | 0.999 | 0.985 | — |
| GABARAPL2 | 0.996 | 0.656 | — |
| GABARAPL1 | 0.995 | 0.478 | — |
| GABARAP | 0.994 | 0.397 | — |
| OPTN | 0.988 | 0.313 | — |
| TBKBP1 | 0.986 | 0.777 | — |
| TBK1 | 0.986 | 0.835 | — |
| SQSTM1 | 0.981 | 0.316 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000258947.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ENKD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF426 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FNDC11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SRI | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FASTK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF408 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DAZAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RHPN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.2 + PDB: 2MXP, 3VVV, 3VVW, 4GXL, 4HAN,  | pLDDT=80.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Cytoplasm, cytoskel / Cytosol; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. CALCOCO2 — Calcium-binding and coiled-coil domain-containing protein 2，研究基础较多，新颖性有限。
2. 蛋白大小446 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 131 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 131 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13137
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136436-CALCOCO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CALCOCO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13137
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000136436-CALCOCO2/subcellular

![](https://images.proteinatlas.org/22989/192_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22989/192_A4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22989/193_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22989/193_A4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22989/194_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22989/194_A4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13137-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
