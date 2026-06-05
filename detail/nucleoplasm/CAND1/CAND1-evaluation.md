---
type: protein-evaluation
gene: "CAND1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CAND1 — REJECTED (研究热度过高 (PubMed strict=137，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAND1 / KIAA0829, TIP120, TIP120A |
| 蛋白名称 | Cullin-associated NEDD8-dissociated protein 1 |
| 蛋白大小 | 1230 aa / 136.4 kDa |
| UniProt ID | Q86VP6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1230 aa / 136.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=137 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=86.8; PDB: 1U6G, 4A0C, 7Z8R, 7Z8T, 7Z8V, 7ZBW, 7ZBZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR039852, IPR013932; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cullin-RING ubiquitin ligase complex (GO:0031461)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 137 |
| PubMed broad count | 179 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0829, TIP120, TIP120A |

**关键文献**:
1. Cullin-associated and neddylation-dissociated protein 1 (CAND1) alleviates NAFLD by reducing ubiquitinated degradation of ACAA2.. *Nature communications*. PMID: 37528093
2. Systemwide disassembly and assembly of SCF ubiquitin ligase complexes.. *Cell*. PMID: 37028429
3. ASCC3 promotes the immunosuppression and progression of non-small cell lung cancer by impairing the type I interferon response via CAND1-mediated ubiquitination inhibition of STAT3.. *Journal for immunotherapy of cancer*. PMID: 38148115
4. Cullin-associated and neddylation-dissociated protein 1 (CAND1) promotes cardiomyocyte proliferation and heart regeneration by enhancing the ubiquitinated degradation of Mps one binder kinase activator 1b (Mob1b).. *Cell death and differentiation*. PMID: 40555744
5. CAND1 mediates CUL7-dependent HER2 protein stability to drive breast cancer progression.. *Breast cancer research : BCR*. PMID: 41310794

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.8 |
| 高置信度残基 (pLDDT>90) 占比 | 52.8% |
| 置信残基 (pLDDT 70-90) 占比 | 40.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 3.7% |
| 有序区域 (pLDDT>70) 占比 | 93.4% |
| 可用 PDB 条目 | 1U6G, 4A0C, 7Z8R, 7Z8T, 7Z8V, 7ZBW, 7ZBZ, 8CDJ, 8CDK, 8H3Q |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1U6G, 4A0C, 7Z8R, 7Z8T, 7Z8V, 7ZBW, 7ZBZ, 8CDJ, 8CDK, 8H3Q）+ AlphaFold极高置信度预测（pLDDT=86.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR039852, IPR013932; Pfam: PF13513, PF08623, PF25782 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL1 | 0.999 | 0.998 | — |
| RBX1 | 0.999 | 0.982 | — |
| CUL4B | 0.997 | 0.979 | — |
| CUL3 | 0.988 | 0.902 | — |
| CUL4A | 0.988 | 0.896 | — |
| CUL2 | 0.981 | 0.837 | — |
| SKP1 | 0.974 | 0.517 | — |
| DCUN1D1 | 0.969 | 0.834 | — |
| NEDD8 | 0.968 | 0.067 | — |
| CUL5 | 0.951 | 0.718 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Irs1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15602769 |
| CUL4B | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:12609982 |
| RBX1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:12609982 |
| CUL4A | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:12609982 |
| CUL3 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:12609982 |
| CUL1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:12609982 |
| CUL2 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:12609982 |
| EBI-1257125 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19463016|imex:IM-17246 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19805454|imex:IM-19495 |
| EBI-6249674 | psi-mi:"MI:0096"(pull down) | pubmed:22623228|imex:IM-17422 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.8 + PDB: 1U6G, 4A0C, 7Z8R, 7Z8T, 7Z8V,  | pLDDT=86.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Golgi apparatus, Cytosol; 额外: Nucleoplasm | 一致 |
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
1. CAND1 — Cullin-associated NEDD8-dissociated protein 1，研究基础较多，新颖性有限。
2. 蛋白大小1230 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 137 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 137 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86VP6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111530-CAND1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CAND1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86VP6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000111530-CAND1/subcellular

![](https://images.proteinatlas.org/55748/873_C3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/55748/873_C3_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/55748/878_C3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55748/878_C3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55748/879_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55748/879_G8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86VP6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
