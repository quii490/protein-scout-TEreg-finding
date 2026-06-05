---
type: protein-evaluation
gene: "PPARA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PPARA — REJECTED (研究热度过高 (PubMed strict=855，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PPARA / NR1C1, PPAR |
| 蛋白名称 | Peroxisome proliferator-activated receptor alpha |
| 蛋白大小 | 468 aa / 52.2 kDa |
| UniProt ID | Q07869 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Primary cilium; 额外: Nucleoli fibrillar center, Nuclear bodie; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 468 aa / 52.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=855 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.2; PDB: 1I7G, 1K7L, 1KKQ, 2NPA, 2P54, 2REW, 2ZNN |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003074, IPR035500, IPR000536, IPR050234, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Primary cilium; 额外: Nucleoli fibrillar center, Nuclear bodies, Centriolar satellite, Basal body | Uncertain |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 855 |
| PubMed broad count | 1699 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NR1C1, PPAR |

**关键文献**:
1. Hepatocyte-specific Mas activation enhances lipophagy and fatty acid oxidation to protect against acetaminophen-induced hepatotoxicity in mice.. *Journal of hepatology*. PMID: 36368597
2. Intestinal peroxisome proliferator-activated receptor α-fatty acid-binding protein 1 axis modulates nonalcoholic steatohepatitis.. *Hepatology (Baltimore, Md.)*. PMID: 35460276
3. YAP-TEAD mediates PPAR α-induced hepatomegaly and liver regeneration in mice.. *Hepatology (Baltimore, Md.)*. PMID: 34387904
4. Activation of PPARA-mediated autophagy reduces Alzheimer disease-like pathology and cognitive decline in a murine model.. *Autophagy*. PMID: 30898012
5. Uncovering the mechanism of resveratrol in the treatment of diabetic kidney disease based on network pharmacology, molecular docking, and experimental validation.. *Journal of translational medicine*. PMID: 37308949

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 64.1% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 21.6% |
| 有序区域 (pLDDT>70) 占比 | 74.1% |
| 可用 PDB 条目 | 1I7G, 1K7L, 1KKQ, 2NPA, 2P54, 2REW, 2ZNN, 3ET1, 3FEI, 3G8I |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1I7G, 1K7L, 1KKQ, 2NPA, 2P54, 2REW, 2ZNN, 3ET1, 3FEI, 3G8I）+ AlphaFold极高置信度预测（pLDDT=80.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003074, IPR035500, IPR000536, IPR050234, IPR001723; Pfam: PF00104, PF00105 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RXRA | 0.999 | 0.840 | — |
| PPARGC1A | 0.999 | 0.959 | — |
| NCOA1 | 0.998 | 0.985 | — |
| NCOR2 | 0.996 | 0.970 | — |
| NCOR1 | 0.991 | 0.833 | — |
| PER2 | 0.989 | 0.091 | — |
| JUN | 0.979 | 0.057 | — |
| LPIN1 | 0.974 | 0.292 | — |
| XPR1 | 0.970 | 0.000 | — |
| FABP1 | 0.964 | 0.253 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STAC3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PRMT2 | psi-mi:"MI:0096"(pull down) | pubmed:12039952 |
| RXRG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| LAMTOR5 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| FOXA3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CDK3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NCOA1 | psi-mi:"MI:0905"(amplified luminescent proximity h | pubmed:21775429|imex:IM-25604 |
| PPARGC1A | psi-mi:"MI:0905"(amplified luminescent proximity h | pubmed:21775429|imex:IM-25604 |
| CREBBP | psi-mi:"MI:0905"(amplified luminescent proximity h | pubmed:21775429|imex:IM-25604 |
| NCOA2 | psi-mi:"MI:0905"(amplified luminescent proximity h | pubmed:21775429|imex:IM-25604 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.2 + PDB: 1I7G, 1K7L, 1KKQ, 2NPA, 2P54,  | pLDDT=80.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Primary cilium; 额外: Nucleoli fibrillar center, Nuc | 一致 |
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
1. PPARA — Peroxisome proliferator-activated receptor alpha，研究基础较多，新颖性有限。
2. 蛋白大小468 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 855 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 855 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q07869
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186951-PPARA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PPARA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q07869
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Primary cilium (uncertain)。来源: https://www.proteinatlas.org/ENSG00000186951-PPARA/subcellular

![](https://images.proteinatlas.org/66941/1288_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66941/1288_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/66941/1492_E10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/66941/1492_E10_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/66941/2149_E8_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/66941/2149_E8_81_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q07869-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
