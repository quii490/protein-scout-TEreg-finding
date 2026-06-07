---
type: protein-evaluation
gene: "NOTCH3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NOTCH3 — REJECTED (研究热度过高 (PubMed strict=1568，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NOTCH3 |
| 蛋白名称 | Neurogenic locus notch homolog protein 3 |
| 蛋白大小 | 2321 aa / 243.6 kDa |
| UniProt ID | Q9UM47 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane; UniProt: Cell membrane; Nucleus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2321 aa / 243.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1568 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.4; PDB: 4ZLP, 5CZV, 5CZX, 6WQU, 6XSW, 8OS0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR000742, IPR001881, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Supported |
| UniProt | Cell membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular region (GO:0005576)
- Golgi membrane (GO:0000139)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- receptor complex (GO:0043235)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1568 |
| PubMed broad count | 2780 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CADASIL: A NOTCH3-associated cerebral small vessel disease.. *Journal of advanced research*. PMID: 38176524
2. CADASIL.. *Handbook of clinical neurology*. PMID: 29478611
3. NOTCH3 promotes malignant progression of bladder cancer by directly regulating SPP1 and activating PI3K/AKT pathway.. *Cell death & disease*. PMID: 39557868
4. Nidogen-2 Maintains the Contractile Phenotype of Vascular Smooth Muscle Cells and Prevents Neointima Formation via Bridging Jagged1-Notch3 Signaling.. *Circulation*. PMID: 34315224
5. Protein aggregates containing wild-type and mutant NOTCH3 are major drivers of arterial pathology in CADASIL.. *The Journal of clinical investigation*. PMID: 38386425

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.4 |
| 高置信度残基 (pLDDT>90) 占比 | 6.5% |
| 置信残基 (pLDDT 70-90) 占比 | 33.3% |
| 中等置信 (pLDDT 50-70) 占比 | 35.2% |
| 低置信 (pLDDT<50) 占比 | 25.0% |
| 有序区域 (pLDDT>70) 占比 | 39.8% |
| 可用 PDB 条目 | 4ZLP, 5CZV, 5CZX, 6WQU, 6XSW, 8OS0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.4），有序残基占 39.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR000742, IPR001881, IPR013032; Pfam: PF00023, PF12796, PF00008 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DLL1 | 0.999 | 0.292 | — |
| JAG2 | 0.999 | 0.368 | — |
| JAG1 | 0.999 | 0.525 | — |
| DLL3 | 0.998 | 0.000 | — |
| DLL4 | 0.998 | 0.000 | — |
| RBPJ | 0.998 | 0.855 | — |
| MAML1 | 0.988 | 0.314 | — |
| MAML3 | 0.986 | 0.071 | — |
| MAML2 | 0.978 | 0.071 | — |
| LFNG | 0.969 | 0.125 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FBLN1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| A0A0F7R8Z5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ald1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ANKRD28 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| Psma1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17292860 |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ENSP00000263388.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| rhsA5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ADAM32 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.4 + PDB: 4ZLP, 5CZV, 5CZX, 6WQU, 6XSW,  | pLDDT=61.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Nucleus / Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NOTCH3 — Neurogenic locus notch homolog protein 3，研究基础较多，新颖性有限。
2. 蛋白大小2321 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 1568 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1568 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UM47
- Protein Atlas: https://www.proteinatlas.org/ENSG00000074181-NOTCH3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NOTCH3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UM47
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000074181-NOTCH3/subcellular

![](https://images.proteinatlas.org/67424/1824_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/67424/1824_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/67424/2050_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/67424/2050_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/67424/2164_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/67424/2164_E9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UM47-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UM47 |
| SMART | SM00248;SM01334;SM00181;SM00179;SM00004;SM01338;SM01339; |
| UniProt Domain [FT] | DOMAIN 40..77; /note="EGF-like 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 78..118; /note="EGF-like 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 119..156; /note="EGF-like 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 158..195; /note="EGF-like 4; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 197..234; /note="EGF-like 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 236..272; /note="EGF-like 6; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 274..312; /note="EGF-like 7"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 314..350; /note="EGF-like 8; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 351..389; /note="EGF-like 9"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 391..429; /note="EGF-like 10; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 431..467; /note="EGF-like 11; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 469..505; /note="EGF-like 12; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 507..543; /note="EGF-like 13; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 545..580; /note="EGF-like 14; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 582..618; /note="EGF-like 15; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 620..655; /note="EGF-like 16; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 657..693; /note="EGF-like 17; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 695..730; /note="EGF-like 18"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 734..770; /note="EGF-like 19"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 771..808; /note="EGF-like 20"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 810..847; /note="EGF-like 21; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 849..885; /note="EGF-like 22; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 887..922; /note="EGF-like 23; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 924..960; /note="EGF-like 24"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 962..998; /note="EGF-like 25"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 1000..1034; /note="EGF-like 26"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 1036..1082; /note="EGF-like 27"; /evidence="ECO:0000305"; DOMAIN 1084..1120; /note="EGF-like 28"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 1122..1158; /note="EGF-like 29; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 1160..1203; /note="EGF-like 30; calcium-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 1205..1244; /note="EGF-like 31"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 1246..1287; /note="EGF-like 32"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 1289..1325; /note="EGF-like 33"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 1335..1373; /note="EGF-like 34"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076" |
| InterPro | IPR002110;IPR036770;IPR000742;IPR001881;IPR013032;IPR000152;IPR018097;IPR009030;IPR008297;IPR035993;IPR051355;IPR049883;IPR022331;IPR024600;IPR000800;IPR010660;IPR011656; |
| Pfam | PF00023;PF12796;PF00008;PF07645;PF12661;PF06816;PF07684;PF00066; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000074181-NOTCH3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HIF1AN | Biogrid, Bioplex | true |
| FBXO2 | Bioplex | false |
| LGALS1 | Bioplex | false |
| NEU2 | Bioplex | false |
| PRG2 | Bioplex | false |
| PRR20D | Intact | false |
| RBPJ | Biogrid | false |
| WWP2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
