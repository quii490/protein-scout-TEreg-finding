---
type: protein-evaluation
gene: "TNIP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TNIP1 — REJECTED (研究热度过高 (PubMed strict=162，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TNIP1 / KIAA0113, NAF1 |
| 蛋白名称 | TNFAIP3-interacting protein 1 |
| 蛋白大小 | 636 aa / 71.9 kDa |
| UniProt ID | Q15025 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 636 aa / 71.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=162 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=70.9; PDB: 7EAL, 7EAO, 7EB9, 8YFK, 8YFL, 8YFM, 8YFN |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 162 |
| PubMed broad count | 286 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0113, NAF1 |

**关键文献**:
1. FTO fuels diabetes-induced vascular endothelial dysfunction associated with inflammation by erasing m6A methylation of TNIP1.. *The Journal of clinical investigation*. PMID: 37781923
2. Targeted proteomics addresses selectivity and complexity of protein degradation by autophagy.. *Autophagy*. PMID: 39245437
3. TNIP1/ABIN1 and lupus nephritis: review.. *Lupus science & medicine*. PMID: 33122334
4. TNIP1 and Autophagy Receptors regulate STING Signaling.. *bioRxiv : the preprint server for biology*. PMID: 40568100
5. Deciphering distinct genetic risk factors for FTLD-TDP pathological subtypes via whole-genome sequencing.. *Nature communications*. PMID: 40280976

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.9 |
| 高置信度残基 (pLDDT>90) 占比 | 39.0% |
| 置信残基 (pLDDT 70-90) 占比 | 17.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 32.7% |
| 有序区域 (pLDDT>70) 占比 | 56.6% |
| 可用 PDB 条目 | 7EAL, 7EAO, 7EB9, 8YFK, 8YFL, 8YFM, 8YFN, 9D34 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7EAL, 7EAO, 7EB9, 8YFK, 8YFL, 8YFM, 8YFN, 9D34）+ AlphaFold极高置信度预测（pLDDT=70.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TNFAIP3 | 0.999 | 0.868 | — |
| TNF | 0.997 | 0.994 | — |
| TNFRSF1A | 0.995 | 0.994 | — |
| UBC | 0.982 | 0.982 | — |
| IKBKG | 0.982 | 0.677 | — |
| NFKB1 | 0.932 | 0.739 | — |
| OPTN | 0.922 | 0.813 | — |
| UBB | 0.900 | 0.900 | — |
| TAX1BP1 | 0.871 | 0.618 | — |
| TNIP2 | 0.821 | 0.225 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000430760.1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| MAGEB18 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RBFOX1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| GIT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| CCNG1 | psi-mi:"MI:0096"(pull down) | imex:IM-15364|pubmed:21988832 |
| GTF2H1 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| OPTN | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NME7 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EFEMP1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.9 + PDB: 7EAL, 7EAO, 7EB9, 8YFK, 8YFL,  | pLDDT=70.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. TNIP1 — TNFAIP3-interacting protein 1，研究基础较多，新颖性有限。
2. 蛋白大小636 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 162 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 162 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15025
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145901-TNIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TNIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15025
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000145901-TNIP1/subcellular

![](https://images.proteinatlas.org/71950/1375_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/71950/1375_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/71950/1384_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/71950/1384_A9_3_red_green.jpg)
![](https://images.proteinatlas.org/71950/1413_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/71950/1413_D10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15025-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
