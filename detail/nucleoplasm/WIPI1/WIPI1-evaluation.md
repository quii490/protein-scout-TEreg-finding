---
type: protein-evaluation
gene: "WIPI1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## WIPI1 — REJECTED (研究热度过高 (PubMed strict=105，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WIPI1 / WIPI49 |
| 蛋白名称 | WD repeat domain phosphoinositide-interacting protein 1 |
| 蛋白大小 | 446 aa / 48.7 kDa |
| UniProt ID | Q5MNZ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytosol; UniProt: Golgi apparatus, trans-Golgi network; Endosome; Cytoplasmic  |
| 蛋白大小 | 10/10 | ×1 | 10 | 446 aa / 48.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=105 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR048720, IPR015943, IPR036322, IPR001680; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **71.5/180** | |
| **归一化总分** | | | **39.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Golgi apparatus, trans-Golgi network; Endosome; Cytoplasmic vesicle, clathrin-coated vesicle; Preaut... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- autophagosome membrane (GO:0000421)
- clathrin-coated vesicle (GO:0030136)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- Golgi membrane (GO:0000139)
- phagophore assembly site (GO:0000407)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 105 |
| PubMed broad count | 147 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WIPI49 |

**关键文献**:
1. The ubiquitin kinase PINK1 recruits autophagy receptors to induce mitophagy.. *Nature*. PMID: 26266977
2. Therapeutic regulation of autophagy in hepatic metabolism.. *Acta pharmaceutica Sinica. B*. PMID: 35127371
3. Identification and analysis of type 2 diabetes-mellitus-associated autophagy-related genes.. *Frontiers in endocrinology*. PMID: 37223013
4. The ABL-MYC axis controls WIPI1-enhanced autophagy in lifespan extension.. *Communications biology*. PMID: 37620393
5. Human WIPI β-propeller function in autophagy and neurodegeneration.. *FEBS letters*. PMID: 38058212

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.9 |
| 高置信度残基 (pLDDT>90) 占比 | 65.2% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 28.7% |
| 有序区域 (pLDDT>70) 占比 | 68.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.9，有序区 68.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048720, IPR015943, IPR036322, IPR001680; Pfam: PF21032 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATG2A | 0.998 | 0.556 | — |
| ATG2B | 0.996 | 0.605 | — |
| ATG16L1 | 0.990 | 0.597 | — |
| ATG16L2 | 0.979 | 0.520 | — |
| WIPI2 | 0.976 | 0.000 | — |
| TECPR1 | 0.974 | 0.000 | — |
| ULK1 | 0.974 | 0.747 | — |
| OTUD7B | 0.962 | 0.000 | — |
| ATG12 | 0.960 | 0.393 | — |
| VAC14 | 0.960 | 0.309 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000262139.4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| PPA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| KCTD15 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| LGALS7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| ATG2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| BECN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| DNASE2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RACK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CEP76 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.9 + PDB: 无 | pLDDT=77.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, trans-Golgi network; Endosome; Cy / Golgi apparatus; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. WIPI1 — WD repeat domain phosphoinositide-interacting protein 1，研究基础较多，新颖性有限。
2. 蛋白大小446 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 105 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 105 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5MNZ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000070540-WIPI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WIPI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5MNZ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000070540-WIPI1/subcellular

![](https://images.proteinatlas.org/37230/1898_B7_21_cr5ba8a9aa349e9_red_green.jpg)
![](https://images.proteinatlas.org/37230/1898_B7_7_cr5ba8a9aa34780_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5MNZ9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
