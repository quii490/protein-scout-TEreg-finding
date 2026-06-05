---
type: protein-evaluation
gene: "STAM2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STAM2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAM2 / HBP |
| 蛋白名称 | Signal transducing adapter molecule 2 |
| 蛋白大小 | 525 aa / 58.2 kDa |
| UniProt ID | O75886 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Early endosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 525 aa / 58.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.6; PDB: 1X2Q, 1X5B, 2L0T, 5CRV, 5IXF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008942, IPR036028, IPR001452, IPR050670, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Early endosome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- early endosome membrane (GO:0031901)
- endocytic vesicle (GO:0030139)
- ESCRT-0 complex (GO:0033565)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 77 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HBP |

**关键文献**:
1. Starvation-induced HBP metabolic reprogramming and STAM2 O-GlcNAcylation facilitate bladder cancer metastasis.. *Scientific reports*. PMID: 40075080
2. Signal-transducing adaptor molecules STAM1 and STAM2 are required for T-cell development and survival.. *Molecular and cellular biology*. PMID: 12446783
3. HSPA1A Protects Cells from Thermal Stress by Impeding ESCRT-0-Mediated Autophagic Flux in Epidermal Thermoresistance.. *The Journal of investigative dermatology*. PMID: 32533962
4. STAM2-mediated fine-tuning of PD-L1 secretion via small extracellular vesicles in oral squamous cell carcinoma.. *International journal of biological macromolecules*. PMID: 40541896
5. Stam2 expression pattern during embryo development.. *Gene expression patterns : GEP*. PMID: 22143071

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.6 |
| 高置信度残基 (pLDDT>90) 占比 | 37.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 39.4% |
| 有序区域 (pLDDT>70) 占比 | 55.2% |
| 可用 PDB 条目 | 1X2Q, 1X5B, 2L0T, 5CRV, 5IXF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.6），有序残基占 55.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008942, IPR036028, IPR001452, IPR050670, IPR035675; Pfam: PF00018, PF02809, PF00790 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HGS | 0.999 | 0.976 | — |
| STAMBP | 0.999 | 0.980 | — |
| UBC | 0.995 | 0.988 | — |
| STAM | 0.994 | 0.804 | — |
| PTPN23 | 0.993 | 0.967 | — |
| USP8 | 0.993 | 0.657 | — |
| JAK3 | 0.990 | 0.313 | — |
| JAK2 | 0.983 | 0.313 | — |
| TSG101 | 0.982 | 0.670 | — |
| RPS27A | 0.976 | 0.946 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HGS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DAZAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| XRN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| L3MBTL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| STAMBP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBQLN4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| PHF10 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| pcm | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| clpB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Crk | psi-mi:"MI:0096"(pull down) | imex:IM-8314|pubmed:20697350|m |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.6 + PDB: 1X2Q, 1X5B, 2L0T, 5CRV, 5IXF | pLDDT=68.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Early endosome membrane / Vesicles; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. STAM2 — Signal transducing adapter molecule 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小525 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75886
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115145-STAM2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAM2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75886
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (supported)。来源: https://www.proteinatlas.org/ENSG00000115145-STAM2/subcellular

![](https://images.proteinatlas.org/35529/574_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/35529/574_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/35529/580_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/35529/580_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/35529/590_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/35529/590_G8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75886-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
