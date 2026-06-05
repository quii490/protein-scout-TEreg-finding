---
type: protein-evaluation
gene: "HUWE1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HUWE1 — REJECTED (研究热度过高 (PubMed strict=255，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HUWE1 / KIAA0312, KIAA1578, UREB1 |
| 蛋白名称 | E3 ubiquitin-protein ligase HUWE1 |
| 蛋白大小 | 4374 aa / 481.9 kDa |
| UniProt ID | Q7Z6Z7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nuclear membrane, Mid piece, Princ; UniProt: Cytoplasm; Nucleus; Mitochondrion |
| 蛋白大小 | 0/10 | ×1 | 0 | 4374 aa / 481.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=255 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 2EKK, 2MUL, 3G1N, 3H1D, 5C6H, 5LP8, 6FYH |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR010309, IPR010314, IPR050409, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65.0/180** | |
| **归一化总分** | | | **36.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nuclear membrane, Mid piece, Principal piece, End piece | Supported |
| UniProt | Cytoplasm; Nucleus; Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)
- mitochondrion (GO:0005739)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 255 |
| PubMed broad count | 412 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0312, KIAA1578, UREB1 |

**关键文献**:
1. Mitochondria ROS and mitophagy in acute kidney injury.. *Autophagy*. PMID: 35678504
2. Role of AMBRA1 in mitophagy regulation: emerging evidence in aging-related diseases.. *Autophagy*. PMID: 39113560
3. KRAS G12C-mutant driven non-small cell lung cancer (NSCLC).. *Critical reviews in oncology/hematology*. PMID: 38072173
4. HUWE1 variants cause dominant X-linked intellectual disability: a clinical study of 21 patients.. *European journal of human genetics : EJHG*. PMID: 29180823
5. Identification of novel mutational drivers reveals oncogene dependencies in multiple myeloma.. *Blood*. PMID: 29884741

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 2EKK, 2MUL, 3G1N, 3H1D, 5C6H, 5LP8, 6FYH, 6MIW, 6PFL, 7AZX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR010309, IPR010314, IPR050409, IPR000569; Pfam: PF06012, PF06025, PF00632 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCL1 | 0.996 | 0.991 | — |
| UBC | 0.979 | 0.971 | — |
| HSD17B10 | 0.975 | 0.292 | — |
| UBE2D2 | 0.957 | 0.832 | — |
| UBB | 0.957 | 0.937 | — |
| DDIT4 | 0.956 | 0.948 | — |
| UBA52 | 0.936 | 0.923 | — |
| RPS27A | 0.934 | 0.909 | — |
| UBE2L3 | 0.921 | 0.865 | — |
| CDKN2A | 0.915 | 0.681 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ptc | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Hsp60B | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19805454|imex:IM-19495 |
| PRKAR1A | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| vif | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| FAF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UBXN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| SLX1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| UBL4A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 2EKK, 2MUL, 3G1N, 3H1D, 5C6H,  | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Mitochondrion / Nucleoplasm, Cytosol; 额外: Nuclear membrane, Mid pi | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HUWE1 — E3 ubiquitin-protein ligase HUWE1，研究基础较多，新颖性有限。
2. 蛋白大小4374 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 255 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 255 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z6Z7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000086758-HUWE1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HUWE1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z6Z7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000086758-HUWE1/subcellular

![](https://images.proteinatlas.org/2548/2209_G11_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/2548/2209_G11_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/22718/667_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/22718/667_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/22718/673_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/22718/673_A2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
