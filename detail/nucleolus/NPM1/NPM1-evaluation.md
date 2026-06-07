---
type: protein-evaluation
gene: "NPM1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NPM1 — REJECTED (研究热度过高 (PubMed strict=1656，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NPM1 / NPM |
| 蛋白名称 | Nucleophosmin |
| 蛋白大小 | 294 aa / 32.6 kDa |
| UniProt ID | P06748 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli rim; 额外: Nucleoplasm; UniProt: Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplasm, cytoske |
| 蛋白大小 | 10/10 | ×1 | 10 | 294 aa / 32.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1656 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.2; PDB: 2LLH, 2P1B, 2VXD, 5EHD, 7OBG, 7OBH, 8AH2 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032569, IPR004301, IPR024057, IPR036824; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli rim; 额外: Nucleoplasm | Enhanced |
| UniProt | Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, ce... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- granular component (GO:0001652)
- large ribosomal subunit (GO:0015934)
- membrane (GO:0016020)
- nuclear speck (GO:0016607)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1656 |
| PubMed broad count | 3777 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NPM |

**关键文献**:
1. MEN1 mutations mediate clinical resistance to menin inhibition.. *Nature*. PMID: 36922589
2. NPM1-mutated acute myeloid leukemia: from bench to bedside.. *Blood*. PMID: 32609823
3. Significance of NPM1 Gene Mutations in AML.. *International journal of molecular sciences*. PMID: 34576201
4. Mutant NPM1 Directly Regulates Oncogenic Transcription in Acute Myeloid Leukemia.. *Cancer discovery*. PMID: 36455613
5. NPM1-mutated acute myeloid leukemia: New pathogenetic and therapeutic insights and open questions.. *American journal of hematology*. PMID: 37317978

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.2 |
| 高置信度残基 (pLDDT>90) 占比 | 37.4% |
| 置信残基 (pLDDT 70-90) 占比 | 16.0% |
| 中等置信 (pLDDT 50-70) 占比 | 20.1% |
| 低置信 (pLDDT<50) 占比 | 26.5% |
| 有序区域 (pLDDT>70) 占比 | 53.4% |
| 可用 PDB 条目 | 2LLH, 2P1B, 2VXD, 5EHD, 7OBG, 7OBH, 8AH2, 8AS5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2LLH, 2P1B, 2VXD, 5EHD, 7OBG, 7OBH, 8AH2, 8AS5）+ AlphaFold极高置信度预测（pLDDT=73.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032569, IPR004301, IPR024057, IPR036824; Pfam: PF16276, PF03066 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCL | 0.999 | 0.844 | — |
| CDKN2A | 0.999 | 0.874 | — |
| TP53 | 0.997 | 0.847 | — |
| ALK | 0.994 | 0.000 | — |
| AGO2 | 0.992 | 0.292 | — |
| HJURP | 0.983 | 0.441 | — |
| H4C6 | 0.980 | 0.796 | — |
| RPL5 | 0.976 | 0.623 | — |
| CTCF | 0.975 | 0.714 | — |
| MDM2 | 0.974 | 0.785 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MED19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| Ncoa6 | psi-mi:"MI:0018"(two hybrid) | pubmed:10866662 |
| ACTB | psi-mi:"MI:0071"(molecular sieving) | pubmed:15047060 |
| TP53 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:12080348 |
| MAP3K14 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RELA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.2 + PDB: 2LLH, 2P1B, 2VXD, 5EHD, 7OBG,  | pLDDT=73.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplas / Nucleoli rim; 额外: Nucleoplasm | 一致 |
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
1. NPM1 — Nucleophosmin，研究基础较多，新颖性有限。
2. 蛋白大小294 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1656 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1656 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P06748
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181163-NPM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NPM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P06748
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli rim (enhanced)。来源: https://www.proteinatlas.org/ENSG00000181163-NPM1/subcellular

![](https://images.proteinatlas.org/11384/108_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/11384/108_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/11384/85_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/11384/85_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/11384/87_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/11384/87_B11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P06748-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P06748 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR032569;IPR004301;IPR024057;IPR036824; |
| Pfam | PF16276;PF03066; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000181163-NPM1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABT1 | Biogrid, Opencell | true |
| BCCIP | Biogrid, Opencell | true |
| BMS1 | Biogrid, Opencell | true |
| BRIX1 | Biogrid, Opencell | true |
| CCDC137 | Biogrid, Opencell | true |
| CCDC8 | Biogrid, Opencell | true |
| CCDC86 | Biogrid, Opencell | true |
| CDKN2A | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
