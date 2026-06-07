---
type: protein-evaluation
gene: "DSP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DSP — REJECTED (研究热度过高 (PubMed strict=1452，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DSP |
| 蛋白名称 | Desmoplakin |
| 蛋白大小 | 2871 aa / 331.8 kDa |
| UniProt ID | P15924 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DSP/IF_images/U-251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DSP/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cell Junctions; UniProt: Cell projection, axon; Cell junction, desmosome; Cell membra |
| 📏 蛋白大小 | 2/10 | ×1 | 2 | 2871 aa / 331.8 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1452 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.2; PDB: 1LM5, 1LM7, 3R6N, 5DZZ |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR041615, IPR041573, IPR043197, IPR035915, IPR001 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.5/180** | |
| **归一化总分** | | | **45.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cell Junctions | Supported |
| UniProt | Cell projection, axon; Cell junction, desmosome; Cell membrane; Cytoplasm; Nucle... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- adherens junction (GO:0005912)
- basolateral plasma membrane (GO:0016323)
- cornified envelope (GO:0001533)
- cytoplasm (GO:0005737)
- desmosome (GO:0030057)
- extracellular exosome (GO:0070062)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1452 |
| PubMed broad count | 6697 |
| 别名(未计入scoring) |  |

**关键文献**:
1. DSP-crosslinking and Immunoprecipitation to Isolate Weak Protein Complex.. *Bio-protocol*. PMID: 36082367
2. Dilated cardiomyopathy and arrhythmogenic left ventricular cardiomyopathy: a comprehensive genotype-imaging phenotype study.. *European heart journal. Cardiovascular Imaging*. PMID: 31317183
3. A novel tool for arrhythmic risk stratification in desmoplakin gene variant carriers.. *European heart journal*. PMID: 39011630
4. Spatial Relationships in the Tumor Microenvironment Demonstrate Association with Pathologic Response to Neoadjuvant Chemoimmunotherapy in Muscle-invasive Bladder Cancer.. *European urology*. PMID: 38092611
5. Dentin matrix proteins.. *European journal of oral sciences*. PMID: 9541227

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 18.7% |
| 置信残基 (pLDDT 70-90) 占比 | 52.7% |
| 中等置信 (pLDDT 50-70) 占比 | 16.4% |
| 低置信 (pLDDT<50) 占比 | 12.2% |
| 有序区域 (pLDDT>70) 占比 | 71.4% |
| 可用 PDB 条目 | 1LM5, 1LM7, 3R6N, 5DZZ |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1LM5, 1LM7, 3R6N, 5DZZ）+ AlphaFold高质量预测（pLDDT=75.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041615, IPR041573, IPR043197, IPR035915, IPR001101; Pfam: PF00681, PF17902, PF18373 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JUP | 0.999 | 0.787 | — |
| PKP2 | 0.999 | 0.440 | — |
| DSG1 | 0.998 | 0.505 | — |
| DSG2 | 0.998 | 0.045 | — |
| DSC2 | 0.998 | 0.294 | — |
| PKP1 | 0.995 | 0.548 | — |
| EVPL | 0.969 | 0.217 | — |
| DSC1 | 0.959 | 0.508 | — |
| KRT18 | 0.957 | 0.612 | — |
| PPL | 0.953 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 1LM5, 1LM7, 3R6N, 5DZZ | pLDDT=75.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell projection, axon; Cell junction, desmosome; C / Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DSP — Desmoplakin，有一定研究基础，但仍存在niche空间。
2. 蛋白大小2871 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 1452 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1452 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P15924
- Protein Atlas: https://www.proteinatlas.org/ENSG00000096696-DSP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DSP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P15924
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:20:09

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P15924 |
| SMART | SM00250;SM00150; |
| UniProt Domain [FT] | DOMAIN 458..515; /note="SH3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192" |
| InterPro | IPR041615;IPR041573;IPR043197;IPR035915;IPR001101;IPR001452;IPR018159; |
| Pfam | PF00681;PF17902;PF18373;PF21019; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000096696-DSP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FES | Intact, Biogrid | true |
| JUP | Intact, Biogrid | true |
| KRT18 | Biogrid, Opencell | true |
| ANLN | Biogrid | false |
| ARAF | Biogrid | false |
| BTRC | Biogrid | false |
| C18orf21 | Bioplex | false |
| C6orf141 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
