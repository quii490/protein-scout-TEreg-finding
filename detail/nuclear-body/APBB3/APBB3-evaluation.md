---
type: protein-evaluation
gene: "APBB3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## APBB3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | APBB3 / FE65L2 |
| 蛋白名称 | Amyloid-beta A4 precursor protein-binding family B member 3 |
| 蛋白大小 | 486 aa / 52.6 kDa |
| UniProt ID | O95704 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Actin filaments; 额外: Cytosol; UniProt: Cytoplasm; Nucleus; Nucleus; Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 486 aa / 52.6 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.5; PDB: 2DYQ, 2YSC |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039576, IPR011993, IPR006020, IPR001202, IPR036 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Actin filaments; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Nucleus; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nuclear body (GO:0016604)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FE65L2 |

**关键文献**:
1. Selection in Australian Thoroughbred horses acts on a locus associated with early two-year old speed.. *PloS one*. PMID: 32049967
2. Integration of Alzheimer's disease genetics and myeloid genomics identifies disease risk regulatory elements and genes.. *Nature communications*. PMID: 33712570
3. Fe65 is the sole member of its family that mediates transcription regulated by the amyloid precursor protein.. *Journal of cell science*. PMID: 32843577
4. Convergence of genes implicated in Alzheimer's disease on the cerebral cholesterol shuttle: APP, cholesterol, lipoproteins, and atherosclerosis.. *Neurochemistry international*. PMID: 16973241
5. Inflammation and neurological disease-related genes are differentially expressed in depressed patients with mood disorders and correlate with morphometric and functional imaging abnormalities.. *Brain, behavior, and immunity*. PMID: 23064081

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.5 |
| 高置信度残基 (pLDDT>90) 占比 | 20.6% |
| 置信残基 (pLDDT 70-90) 占比 | 31.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 38.9% |
| 有序区域 (pLDDT>70) 占比 | 52.3% |
| 可用 PDB 条目 | 2DYQ, 2YSC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.5），有序残基占 52.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039576, IPR011993, IPR006020, IPR001202, IPR036020; Pfam: PF00640, PF00397 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| APP | 0.984 | 0.802 | — |
| APLP2 | 0.803 | 0.650 | — |
| APLP1 | 0.796 | 0.640 | — |
| RHOBTB1 | 0.716 | 0.715 | — |
| COPS4 | 0.702 | 0.702 | — |
| COPS5 | 0.694 | 0.694 | — |
| COPS2 | 0.680 | 0.680 | — |
| COPS7A | 0.677 | 0.670 | — |
| COPS7B | 0.676 | 0.670 | — |
| COPS6 | 0.665 | 0.665 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| App | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:9461550 |
| APLP2 | psi-mi:"MI:0018"(two hybrid) | pubmed:9461550 |
| RAB4A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RBM14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RHOBTB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BLK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APLP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COPS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HGFAC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.5 + PDB: 2DYQ, 2YSC | pLDDT=64.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus; Nucleus / Nuclear bodies, Actin filaments; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 深度机制分析

APBB3（FE65L2）属于FE65蛋白家族，其域架构按照N-WW1-PID1-PID2-C的经典拓扑排列。N端WW结构域（Pfam PF00397、SMART SM00456、InterPro IPR001202）识别富含脯氨酸的PPXY基序，是常规的蛋白-蛋白互作模块。中部串联双磷酸酪氨酸互作域PID1与PID2（Phosphotyrosine Interaction Domain，Pfam PF00640、SMART SM00462、InterPro IPR011993/IPR006020）构成该蛋白的功能核心，PID1负责结合淀粉样前体蛋白（APP）的胞内域（AICD）的YENPTY基序，PID2的配体偏好与PID1不同（可能识别其他含磷酸化酪氨酸的胞内信号分子）。WW-PID共含486 aa（52.6 kDa），属中等大小蛋白，AlphaFold pLDDT为64.5（52.3%有序区域），局部折叠可信，且有PDB条目2DYQ和2YSC的NMR实验结构支持（归一化结构得分9/10中的6分主要受限于PDB仅覆盖部分结构域）。

PPI网络高度集中于APP/APLP蛋白家族（STRING评分APP 984、APLP2 803、APLP1 796），实验互作也以APP和APLP1/2为主（co-IP和酵母双杂交），此外BioGRID检测到EGFR、ERBB2、MOV10和COPS2（COP9信号体亚基2）的互作。MOV10（RNA解旋酶，也是piRNA通路中的重要因子）的互作暗示APBB3可能与小RNA介导的TE沉默存在间接联系。HPA IF明确显示APBB3定位于核体（nuclear bodies），同时存在于细胞质和肌动蛋白骨架。GO-CC确认了nuclear body（GO:0016604）和nucleus（GO:0005634）的定位。

TE调控相关性通过多重间接路径实现：（1）APP/AICD信号级联——APBB3与APP/AICD胞内域结合后，可影响AICD-Fe65-Tip60（KAT5）三元转录激活复合物的核转运和染色质靶向，而Tip60是NuA4乙酰转移酶复合物的催化亚基，负责H4K16ac和H2A.Z的乙酰化——这两者在ERV/LINE-1启动子激活中是关键的表观遗传标记；（2）COPS2——作为COP9信号体亚基，COPS2参与CRL（Cullin-RING Ligase）E3泛素连接酶的活性调控，而CRL复合物介导的蛋白降解可间接影响TE沉默因子（如KAP1/TRIM28）的周转速率；（3）MOV10——MOV10是LINE-1和HERV-K反转录转座过程中的RNA解旋酶，APBB3与MOV10的互作可能影响TE RNA的核输出或RNP复合物的形成；（4）WW-PID双域结构赋予APBB3"信号支架蛋白"的功能——同时结合上游信号分子和下游效应子，可能参与将细胞外信号整合至核内染色质调控。归一化评分72.5/100，MOV10和APP-AICD-Tip60轴赋予其适度的TE调控潜力。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. APBB3 — Amyloid-beta A4 precursor protein-binding family B member 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小486 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | STRING | 984 |
| APLP1 | STRING | 796 |
| RHOBTB1 | STRING | 716 |
| COPS4 | STRING | 702 |
| EGFR | BioGRID | 1 |
| ERBB2 | BioGRID | 1 |
| MOV10 | BioGRID | 1 |
| COPS2 | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95704
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113108-APBB3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=APBB3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95704
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:58:37

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000113108-APBB3/subcellular

![](https://images.proteinatlas.org/5571/2144_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5571/2144_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/5571/2189_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/5571/2189_D2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/5571/73_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5571/73_B9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95704-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95704 |
| SMART | SM00462;SM00456; |
| UniProt Domain [FT] | DOMAIN 29..61; /note="WW"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00224"; DOMAIN 113..280; /note="PID 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00148"; DOMAIN 285..440; /note="PID 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00148" |
| InterPro | IPR039576;IPR011993;IPR006020;IPR001202;IPR036020; |
| Pfam | PF00640;PF00397; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000113108-APBB3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APLP2 | Intact, Biogrid | true |
| APP | Intact, Biogrid | true |
| DAPP1 | Intact, Biogrid | true |
| APLP1 | Biogrid | false |
| COPS4 | Bioplex | false |
| COPS5 | Bioplex | false |
| COPS6 | Bioplex | false |
| COPS7B | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
