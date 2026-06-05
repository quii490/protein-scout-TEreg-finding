---
type: protein-evaluation
gene: "NHEJ1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NHEJ1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NHEJ1 / XLF |
| 蛋白名称 | Non-homologous end-joining factor 1 |
| 蛋白大小 | 299 aa / 33.3 kDa |
| UniProt ID | Q9H9Q4 |
| 数据采集时间 | 2026-06-03 23:42:16 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | x1 | 10 | 299 aa / 33.3 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=55 篇 (41-60 -> 6) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=81.8; PDB: 2QM4, 2R9A, 3Q4F, 3RWR, 3SR2, 3W03, |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR052287, IPR053829, IPR015381, IPR038051; P |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 6 interactions |
| 互证加分 | -- | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- DNA ligase IV complex (GO:0032807)
- DNA-dependent protein kinase-DNA ligase 4 complex (GO:0005958)
- fibrillar center (GO:0001650)
- nonhomologous end joining complex (GO:0070419)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 55 |
| PubMed broad count | 185 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: XLF |

**关键文献**:
1. Loss of NHEJ1 Protein Due to a Novel Splice Site Mutation in a Family Presenting with Combined Immunodeficiency, Microcephaly, and Growth Retardation and Literature Review.. *Journal of clinical immunology*. PMID: 28741180
2. Nijmegen breakage syndrome (NBS).. *Orphanet journal of rare diseases*. PMID: 22373003
3. DNA Damage Response Genes in Osteosarcoma.. *Journal of oncology*. PMID: 35251167
4. Genotypic and allelic frequency of a mutation in the NHEJ1 gene associated with collie eye anomaly in dogs in Italy.. *Veterinary record open*. PMID: 35127102
5. Clinical variability and novel mutations in the NHEJ1 gene in patients with a Nijmegen breakage syndrome-like phenotype.. *Human mutation*. PMID: 20597108

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 64.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 19.4% |
| 有序区域 (pLDDT>70) 占比 | 77.2% |
| 可用 PDB 条目 | 2QM4, 2R9A, 3Q4F, 3RWR, 3SR2, 3W03, 6ERG, 6ERH, 7LSY, 7LT3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2QM4, 2R9A, 3Q4F, 3RWR, 3SR2, 3W03, 6ERG, 6ERH, 7LSY, 7LT3）+ AlphaFold预测（pLDDT=81.8），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052287, IPR053829, IPR015381, IPR038051; Pfam: PF09302, PF21928 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q96JS9 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:16439205|imex:IM-11818 |
| XRCC4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16439205|imex:IM-11818 |
| LIG4 | psi-mi:"MI:0096"(pull down) | pubmed:16439205|imex:IM-11818 |
| IGBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Sgo1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| EBI-2533263 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-30341|pubmed:40739040 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 6
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 2QM4, 2R9A, 3Q4F, 3RWR, 3SR2,  | pLDDT=81.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 0 + 6 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. NHEJ1 -- Non-homologous end-joining factor 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小299 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 55 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H9Q4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187736-NHEJ1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NHEJ1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H9Q4
- STRING: https://string-db.org/network/9606.NHEJ1
- Packet data timestamp: 2026-06-03 23:42:16

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000187736-NHEJ1/subcellular

![](https://images.proteinatlas.org/43869/1309_D12_4_red_green.jpg)
![](https://images.proteinatlas.org/43869/1309_D12_5_red_green.jpg)
![](https://images.proteinatlas.org/43869/807_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/43869/807_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/43869/846_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/43869/846_E3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H9Q4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
