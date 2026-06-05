---
type: protein-evaluation
gene: "PLK4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PLK4 — REJECTED (研究热度过高 (PubMed strict=301，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLK4 / SAK, STK18 |
| 蛋白名称 | Serine/threonine-protein kinase PLK4 |
| 蛋白大小 | 970 aa / 109.0 kDa |
| UniProt ID | O00444 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centrosome; 额外: Cytosol; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 8/10 | ×1 | 8 | 970 aa / 109.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=301 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.6; PDB: 2N19, 3COK, 4JXF, 4N7V, 4N7Z, 4N9J, 4YUR |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR047108, IPR000959, IPR033699, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome; 额外: Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; Nucleus, nucleolus; C... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriole (GO:0005814)
- centrosome (GO:0005813)
- cleavage furrow (GO:0032154)
- cytosol (GO:0005829)
- deuterosome (GO:0098536)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)
- procentriole (GO:0120098)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 301 |
| PubMed broad count | 591 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SAK, STK18 |

**关键文献**:
1. TRIM37 controls cancer-specific vulnerability to PLK4 inhibition.. *Nature*. PMID: 32908304
2. CRISPR screens reveal convergent targeting strategies against evolutionarily distinct chemoresistance in cancer.. *Nature communications*. PMID: 38951519
3. Inhibition of PLK4 remodels histone methylation and activates the immune response via the cGAS-STING pathway in TP53-mutated AML.. *Blood*. PMID: 37738460
4. BCAT1 Activation Reprograms Branched-Chain Amino Acid Metabolism and Epigenetically Promotes Inflammation in Diabetic Retinopathy.. *Investigative ophthalmology & visual science*. PMID: 40530920
5. Building a centriole.. *Current opinion in cell biology*. PMID: 23199753

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.6 |
| 高置信度残基 (pLDDT>90) 占比 | 35.6% |
| 置信残基 (pLDDT 70-90) 占比 | 20.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 40.4% |
| 有序区域 (pLDDT>70) 占比 | 55.9% |
| 可用 PDB 条目 | 2N19, 3COK, 4JXF, 4N7V, 4N7Z, 4N9J, 4YUR, 4YYP, 5LHY, 5LHZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.6），有序残基占 55.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR047108, IPR000959, IPR033699, IPR033698; Pfam: PF00069, PF18190, PF18409 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CEP192 | 0.999 | 0.976 | — |
| CEP152 | 0.999 | 0.982 | — |
| STIL | 0.999 | 0.961 | — |
| SASS6 | 0.997 | 0.420 | — |
| CENPJ | 0.996 | 0.554 | — |
| CEP135 | 0.988 | 0.356 | — |
| CCP110 | 0.964 | 0.072 | — |
| PLK1 | 0.956 | 0.193 | — |
| CDK1 | 0.946 | 0.133 | — |
| BUB1B | 0.935 | 0.151 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000270861.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SFN | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| TENT5C | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MTUS2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TAX1BP3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EBI-1380996 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| EBI-1381002 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| EBI-1380972 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38943" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.6 + PDB: 2N19, 3COK, 4JXF, 4N7V, 4N7Z,  | pLDDT=65.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Centrosome; 额外: Cytosol | 一致 |
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
1. PLK4 — Serine/threonine-protein kinase PLK4，研究基础较多，新颖性有限。
2. 蛋白大小970 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 301 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 301 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00444
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142731-PLK4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLK4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00444
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (supported)。来源: https://www.proteinatlas.org/ENSG00000142731-PLK4/subcellular

![](https://images.proteinatlas.org/17327/1634_F3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17327/1634_F3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17327/1717_C11_13_cr57f4f3933d450_blue_red_green.jpg)
![](https://images.proteinatlas.org/17327/1717_C11_16_cr57f4f39cb500f_blue_red_green.jpg)
![](https://images.proteinatlas.org/17327/2128_E4_14_blue_red_green.jpg)
![](https://images.proteinatlas.org/17327/2128_E4_56_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00444-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
