---
type: protein-evaluation
gene: "DIDO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DIDO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DIDO1 / C20orf158, DATF1, KIAA0333 |
| 蛋白名称 | Death-inducer obliterator 1 |
| 蛋白大小 | 2240 aa / 243.9 kDa |
| UniProt ID | Q9BTC0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, spindle |
| 蛋白大小 | 2/10 | ×1 | 2 | 2240 aa / 243.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=46.1; PDB: 2M3H, 4L7X |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033082, IPR012921, IPR003618, IPR036575, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.5/180** | |
| **归一化总分** | | | **62.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 68 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf158, DATF1, KIAA0333 |

**关键文献**:
1. Large-scale exome sequence analysis identifies sex- and age-specific determinants of obesity.. *Cell genomics*. PMID: 37601970
2. CircDIDO1 inhibits gastric cancer progression by encoding a novel DIDO1-529aa protein and regulating PRDX2 protein stability.. *Molecular cancer*. PMID: 34384442
3. DIDO is necessary for the adipogenesis that promotes diet-induced obesity.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38194457
4. Serum anti-DIDO1, anti-CPSF2, and anti-FOXJ2 antibodies as predictive risk markers for acute ischemic stroke.. *BMC medicine*. PMID: 34103026
5. CSE1L, DIDO1 and RBM39 in colorectal adenoma to carcinoma progression.. *Cellular oncology (Dordrecht, Netherlands)*. PMID: 22711543

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 46.1 |
| 高置信度残基 (pLDDT>90) 占比 | 7.6% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 75.4% |
| 有序区域 (pLDDT>70) 占比 | 19.8% |
| 可用 PDB 条目 | 2M3H, 4L7X |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=46.1），有序残基占 19.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033082, IPR012921, IPR003618, IPR036575, IPR019786; Pfam: PF00628, PF07744, PF07500 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H3-4 | 0.980 | 0.927 | — |
| H3C12 | 0.967 | 0.934 | — |
| H3-3B | 0.964 | 0.927 | — |
| H3-5 | 0.963 | 0.927 | — |
| H3-2 | 0.963 | 0.927 | — |
| H3C13 | 0.963 | 0.927 | — |
| H3C1 | 0.945 | 0.942 | — |
| H3C8 | 0.936 | 0.927 | — |
| H3C14 | 0.933 | 0.927 | — |
| H3C7 | 0.932 | 0.927 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SRSF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| WWP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| WWP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HNRNPK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DVL3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TNKS2 | psi-mi:"MI:0053"(fluorescence polarization spectro | pubmed:22153077|imex:IM-16612 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| ARAF | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| KCNK4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=46.1 + PDB: 2M3H, 4L7X | pLDDT=46.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, spind / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DIDO1 — Death-inducer obliterator 1，非常新颖，仅有少数基础研究。
2. 蛋白大小2240 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=46.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BTC0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101191-DIDO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DIDO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BTC0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000101191-DIDO1/subcellular

![](https://images.proteinatlas.org/4374/646_H9_3_red_green.jpg)
![](https://images.proteinatlas.org/4374/646_H9_4_red_green.jpg)
![](https://images.proteinatlas.org/4374/663_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/4374/663_H9_5_red_green.jpg)
![](https://images.proteinatlas.org/4374/672_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/4374/672_H9_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BTC0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
