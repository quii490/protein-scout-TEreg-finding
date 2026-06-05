---
type: protein-evaluation
gene: "GLUL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GLUL — REJECTED (研究热度过高 (PubMed strict=198，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLUL / GLNS |
| 蛋白名称 | Glutamine synthetase |
| 蛋白大小 | 373 aa / 42.1 kDa |
| UniProt ID | P15104 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria, Cytosol; 额外: Plasma membrane, Connecting piece; UniProt: Cytoplasm, cytosol; Microsome; Mitochondrion; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 373 aa / 42.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=198 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.5; PDB: 2OJW, 2QC8, 7EVT, 8DNU, 9OTM, 9OTN, 9OTO |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008147, IPR036651, IPR014746, IPR008146, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria, Cytosol; 额外: Plasma membrane, Connecting piece | Approved |
| UniProt | Cytoplasm, cytosol; Microsome; Mitochondrion; Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell body (GO:0044297)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- glial cell projection (GO:0097386)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 198 |
| PubMed broad count | 331 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GLNS |

**关键文献**:
1. High dietary fructose promotes hepatocellular carcinoma progression by enhancing O-GlcNAcylation via microbiota-derived acetate.. *Cell metabolism*. PMID: 37797623
2. SIRT5 regulation of ammonia-induced autophagy and mitophagy.. *Autophagy*. PMID: 25700560
3. Role of glutamine synthetase in angiogenesis beyond glutamine synthesis.. *Nature*. PMID: 30158707
4. PHF8-GLUL axis in lipid deposition and tumor growth of clear cell renal cell carcinoma.. *Science advances*. PMID: 37531433
5. SIRT6 promotes intrahepatic cholangiocarcinoma development by reprogramming glutamine metabolism via enhanced GLUL.. *Gut*. PMID: 41136182

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.5 |
| 高置信度残基 (pLDDT>90) 占比 | 97.1% |
| 置信残基 (pLDDT 70-90) 占比 | 2.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.5% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.5% |
| 可用 PDB 条目 | 2OJW, 2QC8, 7EVT, 8DNU, 9OTM, 9OTN, 9OTO, 9OTP, 9OTQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2OJW, 2QC8, 7EVT, 8DNU, 9OTM, 9OTN, 9OTO, 9OTP, 9OTQ）+ AlphaFold极高置信度预测（pLDDT=97.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008147, IPR036651, IPR014746, IPR008146, IPR027303; Pfam: PF00120, PF03951 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GLUD1 | 0.991 | 0.000 | — |
| GLS2 | 0.987 | 0.000 | — |
| GLS | 0.987 | 0.000 | — |
| GLUD2 | 0.985 | 0.000 | — |
| RIPK3 | 0.974 | 0.045 | — |
| PPAT | 0.973 | 0.000 | — |
| CPS1 | 0.972 | 0.000 | — |
| CAD | 0.967 | 0.000 | — |
| GFPT1 | 0.965 | 0.000 | — |
| GFPT2 | 0.963 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000398320.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Btk | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| NUDT18 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PLEKHF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Dynll1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14760703 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NFKB1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RABEPK | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CYP39A1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| acnA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.5 + PDB: 2OJW, 2QC8, 7EVT, 8DNU, 9OTM,  | pLDDT=97.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Microsome; Mitochondrion; Cell / Mitochondria, Cytosol; 额外: Plasma membrane, Connec | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GLUL — Glutamine synthetase，研究基础较多，新颖性有限。
2. 蛋白大小373 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 198 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 198 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P15104
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135821-GLUL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLUL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P15104
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000135821-GLUL/subcellular

![](https://images.proteinatlas.org/7316/2229_F9_21_blue_red_green.jpg)
![](https://images.proteinatlas.org/7316/2229_F9_44_blue_red_green.jpg)
![](https://images.proteinatlas.org/8636/634_C3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8636/634_C3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8636/635_C3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8636/635_C3_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P15104-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
