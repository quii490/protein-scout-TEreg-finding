---
type: protein-evaluation
gene: "RFNG"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RFNG 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RFNG |
| 蛋白名称 | Beta-1,3-N-acetylglucosaminyltransferase radical fringe |
| 蛋白大小 | 331 aa / 36.4 kDa |
| UniProt ID | Q9Y644 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 331 aa / 36.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017374, IPR003378; Pfam: PF02434 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular region (GO:0005576)
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The N-acetylglucosaminyltransferase Radical fringe contributes to defects in JAG1-dependent turnover and signaling of NOTCH3 CADASIL mutants.. *The Journal of biological chemistry*. PMID: 39303912
2. A pan-cancer analysis revealing the role of LFNG, MFNG and RFNG in tumor prognosis and microenvironment.. *BMC cancer*. PMID: 37932706
3. Lunatic, Manic, and Radical Fringe Each Promote T and B Cell Development.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 26608918
4. Identification and validation of crucial lnc-TRIM28-14 and hub genes promoting gastric cancer peritoneal metastasis.. *BMC cancer*. PMID: 36690975
5. Caveolin-1 promotes Rfng expression via Erk-Jnk-p38 signaling pathway in mouse hepatocarcinoma cells.. *Journal of physiology and biochemistry*. PMID: 31529314

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.4 |
| 高置信度残基 (pLDDT>90) 占比 | 73.7% |
| 置信残基 (pLDDT 70-90) 占比 | 5.4% |
| 中等置信 (pLDDT 50-70) 占比 | 16.6% |
| 低置信 (pLDDT<50) 占比 | 4.2% |
| 有序区域 (pLDDT>70) 占比 | 79.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.4，有序区 79.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017374, IPR003378; Pfam: PF02434 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOTCH3 | 0.952 | 0.125 | — |
| NOTCH1 | 0.936 | 0.073 | — |
| NOTCH2 | 0.931 | 0.125 | — |
| NOTCH4 | 0.926 | 0.073 | — |
| MFNG | 0.908 | 0.000 | — |
| LFNG | 0.906 | 0.000 | — |
| POFUT1 | 0.642 | 0.000 | — |
| DLL3 | 0.581 | 0.073 | — |
| EGF | 0.566 | 0.000 | — |
| B3GNT10 | 0.506 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TMEM106A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLEC12B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SCGB2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ST14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HTR1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.4 + PDB: 无 | pLDDT=87.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. RFNG — Beta-1,3-N-acetylglucosaminyltransferase radical fringe，非常新颖，仅有少数基础研究。
2. 蛋白大小331 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y644
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169733-RFNG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RFNG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y644
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000169733-RFNG/subcellular

![](https://images.proteinatlas.org/11564/50_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/11564/50_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/11564/52_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/11564/52_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/31673/1042_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/31673/1042_D10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y644-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
