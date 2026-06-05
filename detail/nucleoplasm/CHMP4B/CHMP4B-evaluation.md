---
type: protein-evaluation
gene: "CHMP4B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CHMP4B — REJECTED (研究热度过高 (PubMed strict=123，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHMP4B / C20orf178, SHAX1 |
| 蛋白名称 | Charged multivesicular body protein 4b |
| 蛋白大小 | 224 aa / 24.9 kDa |
| UniProt ID | Q9H444 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol; Late endosome membrane; Midbody; Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 224 aa / 24.9 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=123 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=78.9; PDB: 3C3Q, 3UM3, 4ABM, 5MK2 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR005024; Pfam: PF03357 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytosol; Late endosome membrane; Midbody; Nucleus envelope | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- amphisome membrane (GO:1904930)
- autophagosome membrane (GO:0000421)
- cytoplasm (GO:0005737)
- cytoplasmic side of plasma membrane (GO:0009898)
- cytosol (GO:0005829)
- endosome (GO:0005768)
- ESCRT III complex (GO:0000815)
- extracellular exosome (GO:0070062)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 123 |
| PubMed broad count | 192 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf178, SHAX1 |

**关键文献**:
1. Restoration of lysosomal function attenuates autophagic flux impairment in nucleus pulposus cells and protects against mechanical overloading-induced intervertebral disc degeneration.. *Autophagy*. PMID: 39675125
2. ATP6V1D drives hepatocellular carcinoma stemness and progression via both lysosome acidification-dependent and -independent mechanisms.. *Autophagy*. PMID: 39316516
3. Regulating the balance between GSDMD-mediated pyroptosis and CHMP4B-dependent cell repair attenuates calcium oxalate kidney stone formation.. *International journal of biological sciences*. PMID: 40384863
4. Classical swine fever virus hijacks ESCRT-III and VPS4A to promote phagophore closure for accelerating mitophagy.. *Autophagy*. PMID: 40574328
5. Charged multivesicular body protein 4b forms complexes with gap junction proteins during lens fiber cell differentiation.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 36880430

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.9 |
| 高置信度残基 (pLDDT>90) 占比 | 43.3% |
| 置信残基 (pLDDT 70-90) 占比 | 28.6% |
| 中等置信 (pLDDT 50-70) 占比 | 12.9% |
| 低置信 (pLDDT<50) 占比 | 15.2% |
| 有序区域 (pLDDT>70) 占比 | 71.9% |
| 可用 PDB 条目 | 3C3Q, 3UM3, 4ABM, 5MK2 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3C3Q, 3UM3, 4ABM, 5MK2）+ AlphaFold高质量预测（pLDDT=78.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005024; Pfam: PF03357 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDCD6IP | 0.998 | 0.972 | — |
| CHMP3 | 0.998 | 0.949 | — |
| CHMP2A | 0.996 | 0.924 | — |
| CHMP6 | 0.995 | 0.918 | — |
| CHMP1B | 0.994 | 0.910 | — |
| PTPN23 | 0.994 | 0.980 | — |
| CHMP2B | 0.989 | 0.669 | — |
| BROX | 0.984 | 0.975 | — |
| VPS25 | 0.974 | 0.411 | — |
| CHMP4C | 0.973 | 0.739 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000217402.2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-24991|pubmed:16730941 |
| UBE2I | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| KCNMA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-15154|pubmed:22174833 |
| Chmp3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PRKAR1A | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ATP6V1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21674799|imex:IM-16565 |
| EBI-1257121 | psi-mi:"MI:0400"(affinity technology) | pubmed:19367725|imex:IM-20587 |
| COX15 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.9 + PDB: 3C3Q, 3UM3, 4ABM, 5MK2 | pLDDT=78.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Late endosome membrane; Midbod / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CHMP4B -- Charged multivesicular body protein 4b，研究基础较多，新颖性有限。
2. 蛋白大小224 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 123 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 123 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H444
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101421-CHMP4B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHMP4B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H444
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H444-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
