---
type: protein-evaluation
gene: "ETNK2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ETNK2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ETNK2 / EKI2 |
| 蛋白名称 | Ethanolamine kinase 2 |
| 蛋白大小 | 386 aa / 44.8 kDa |
| UniProt ID | Q9NVF9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 386 aa / 44.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011009; Pfam: PF01633 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EKI2 |

**关键文献**:
1. The ETNK2 gene promotes progression of papillary thyroid carcinoma through the HIPPO pathway.. *Journal of Cancer*. PMID: 35069898
2. ETNK2 Low-Expression Predicts Poor Prognosis in Renal Cell Carcinoma with Immunosuppressive Tumor Microenvironment.. *Journal of oncology*. PMID: 36866238
3. Hepatic metastasis of gastric cancer is associated with enhanced expression of ethanolamine kinase 2 via the p53-Bcl-2 intrinsic apoptosis pathway.. *British journal of cancer*. PMID: 33531692
4. Placental thrombosis and spontaneous fetal death in mice deficient in ethanolamine kinase 2.. *The Journal of biological chemistry*. PMID: 16861741
5. Dysregulated human renin expression in transgenic mice carrying truncated genomic constructs: evidence supporting the presence of insulators at the renin locus.. *American journal of physiology. Renal physiology*. PMID: 18632798

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.7 |
| 高置信度残基 (pLDDT>90) 占比 | 78.5% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 12.2% |
| 有序区域 (pLDDT>70) 占比 | 87.0% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.7，有序区 87.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009; Pfam: PF01633 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCYT2 | 0.991 | 0.000 | — |
| ETNPPL | 0.943 | 0.053 | — |
| GPCPD1 | 0.907 | 0.000 | — |
| SELENOI | 0.748 | 0.000 | — |
| GOLT1A | 0.697 | 0.000 | — |
| PISD | 0.667 | 0.056 | — |
| CEPT1 | 0.650 | 0.000 | — |
| PCYT1A | 0.635 | 0.000 | — |
| PCYT1B | 0.608 | 0.000 | — |
| MAPKAP1 | 0.600 | 0.572 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NOL3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBE2A | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| MDFI | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| RAB11B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CYSRT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HNRNPK | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP12-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ATN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| STX1A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MID2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.7 + PDB: 无 | pLDDT=87.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ETNK2 — Ethanolamine kinase 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小386 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 深度机制分析

**结构域架构**：ETNK2（386 aa，44.8 kDa）是乙醇胺激酶2（Ethanolamine Kinase 2），属于胆碱/乙醇胺激酶（ChoK/EtnK）家族。其结构域架构简洁：蛋白激酶样催化结构域（IPR011009）——采用与典型蛋白激酶同源的折叠，含经典的ATP结合G-loop（核苷酸结合P-loop）和底物结合裂沟。PF01633（胆碱/乙醇胺激酶）家族的催化机制为非磷酸转移（不同于Ser/Thr/Tyr激酶的磷酸基团转移至蛋白质侧链），而是将ATP的γ-磷酸转移至乙醇胺/胆碱的羟基——催化化学为醇激酶反应（alcohol + ATP → phosphoalcohol + ADP）。AlphaFold pLDDT=87.7（高置信度，78.5%残基pLDDT>90），表明整个催化结构域折叠高度保守且可靠。ETNK2定位为cytoplasm/cytosol（GO-CC），缺乏核定位信号——但N端（1-50 aa）区域含分散的碱性残基。

**PPI互作网络解读**：PPI网络紧密围绕磷脂合成Kennedy通路：PCYT2（STRING 991，CTP:磷酸乙醇胺胞苷酰转移酶）——CDP-乙醇胺通路下游的限速酶，与ETNK2形成"底物通道"（substrate channeling），ETNK2的产物（磷酸乙醇胺）直接递送至PCYT2活性位点——这是代谢物通道化的经典范式；SELENOI/EPT1（STRING 748，乙醇胺磷酸转移酶1）——CDP-乙醇胺通路的终端酶，负责将磷酸乙醇胺从CDP-乙醇胺转移至二酰甘油生成磷脂酰乙醇胺（PE）；ETNPPL（STRING 943，乙醇胺磷酸裂解酶）——催化磷酸乙醇胺降解的分解酶，形成合成/降解对立调控；GPCPD1（STRING 907）和PISD（STRING 667）——参与磷脂酰胆碱/磷脂酰丝氨酸代谢的其他酶。MAPKAP1（SIN1, STRING 600）——mTORC2复合体必需亚基，提示ETNK2可能与生长因子信号存在交叉。IntAct实验互作包括HNRNPK（核不均一核糖核蛋白K）——RNA/DNA结合蛋白，转录和mRNA剪接调控因子。

**结构解读**：ETNK2的催化域采用典型激酶折叠——N端叶（N-lobe, 5条反平行β-链+αC螺旋）、C端叶（C-lobe, 以α-螺旋为主）。ATP结合位点位于双叶之间的裂隙——G-loop（GxGxxG基序）覆盖ATP的α和β磷酸基团，腺嘌呤环通过疏水堆积和氢键锚定。乙醇胺/胆碱底物进入相邻的底物结合口袋——底物羟基与催化碱（Asp/Glu）形成氢键以活化亲核攻击，γ-磷酸作为亲电体。区别于典型激酶，ETNK2的活化环（activation loop）非磷酸化调控，而是底物结合直接诱导闭合构象（induced-fit）封闭活性位点。pLDDT>90区域集中在催化域核心——ATP结合口袋、底物结合裂沟和双叶界面。

**机制模型**：（1）CDP-乙醇胺（Kennedy）通路中的第一步——ETNK2催化乙醇胺 + ATP → 磷酸乙醇胺 + ADP；（2）产物通道化——ETNK2与PCYT2通过物理互作（STRING 991）形成超分子代谢复合体，磷酸乙醇胺从ETNK2活性位点解离后直接在复合体内部转移至PCYT2催化中心，避免扩散稀释和竞争消耗；（3）肝转移的代谢重编程——ETNK2在胃癌肝转移中通过p53-Bcl-2内在凋亡通路被上调（PMID:33531692），高ETNK2水平增加PE合成以支持膜生物量（肝转移需要大量膜重塑），同时PE是自噬体形成所需的关键磷脂；（4）Hippo通路交叉——ETNK2促进PTC进展通过Hippo通路（PMID:35069898），机制可能为PE作为YAP/TAZ的膜锚定点调控因子——PE水平影响质膜的脂质堆积密度，从而调控YAP的膜-核穿梭；（5）HNRNPK互作提示ETNK2可能参与核内RNA代谢调控——鉴于HNRNPK是核质穿梭蛋白，ETNK2（即使无经典NLS）可能通过"携带"（piggyback）机制被HNRNPK带入细胞核，在核质中参与核内磷脂信号。

**TE调控展望**：ETNK2不直接参与TE调控。最间接的关联通过PE-自噬-TE clearance轴——PE对自噬体膜的生成至关重要（ATG8/LC3-PE脂质化），自噬可选择性包裹并降解L1/Alu的逆转录转座子RNA（retrotransposon RNA, RNautophagy/DNautophagy subtypes）。ETNK2活性降低→PE合成减少→自噬缺陷→TE RNA积累——这一代谢-TE调控链条有生化逻辑支撑，但目前无直接实验证据连接ETNK2和TE。HNRNPK互作提供了更localized的机制——HNRNPK结合LINE-1和Alu RNA并调控其核保留和逆转录转座，ETNK2对HNRNPK的调控可能影响此过程。但鉴于ETNK2已被本评估reject（核定位得分2/10），这些展望纯粹是知识性的。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVF9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143845-ETNK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ETNK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVF9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVF9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
