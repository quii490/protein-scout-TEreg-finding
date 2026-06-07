---
type: protein-evaluation
gene: "DST"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DST — REJECTED (研究热度过高 (PubMed strict=598，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DST / BP230, BP240, BPAG1, DMH, DT |
| 蛋白名称 | Dystonin |
| 蛋白大小 | 7570 aa / 860.7 kDa |
| UniProt ID | Q03001 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Microtubules; 额外: Cytosol; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, stress fib |
| 📏 蛋白大小 | 0/10 | ×1 | 0 | 7570 aa / 860.7 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=598 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.5; PDB: 3GJO, 7OLG |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001589, IPR001715, IPR036872, IPR041615, IPR041 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **70.0/180** | |
| **归一化总分** | | | **38.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Microtubules; 额外: Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, stress fiber; Cell projection,... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- axon (GO:0030424)
- axon cytoplasm (GO:1904115)
- basal plasma membrane (GO:0009925)
- basement membrane (GO:0005604)
- cell cortex (GO:0005938)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 598 |
| PubMed broad count | 17626 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BP230, BP240, BPAG1, DMH, DT, KIAA0728 |

**关键文献**:
1. Drug-resistant Spinal Tuberculosis.. *Indian journal of orthopaedics*. PMID: 29576636
2. The DST gene in neurobiology.. *Journal of neurogenetics*. PMID: 38465459
3. Deciphering DST-associated disorders: biallelic variants affecting DST-b cause a congenital myopathy.. *Brain : a journal of neurology*. PMID: 40497796
4. Microbiological profile of slow-growing non-tuberculous mycobacteria species other than Mycobacterium avium complex.. *Frontiers in microbiology*. PMID: 40351313
5. Cycloserine resistance among drug-resistant tuberculosis cases in Taiwan.. *Microbiology spectrum*. PMID: 40488463

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.5 |
| 高置信度残基 (pLDDT>90) 占比 | 9.1% |
| 置信残基 (pLDDT 70-90) 占比 | 45.7% |
| 中等置信 (pLDDT 50-70) 占比 | 22.7% |
| 低置信 (pLDDT<50) 占比 | 22.5% |
| 有序区域 (pLDDT>70) 占比 | 54.8% |
| 可用 PDB 条目 | 3GJO, 7OLG |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.5），有序残基占 54.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001589, IPR001715, IPR036872, IPR041615, IPR041573; Pfam: PF00307, PF13499, PF02187 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COL17A1 | 0.999 | 0.491 | — |
| PLEC | 0.998 | 0.000 | — |
| CD151 | 0.991 | 0.000 | — |
| ITGB4 | 0.991 | 0.349 | — |
| MAPRE1 | 0.988 | 0.983 | — |
| DSG3 | 0.870 | 0.045 | — |
| ERBIN | 0.847 | 0.304 | — |
| LAMA3 | 0.839 | 0.053 | — |
| DSG1 | 0.837 | 0.045 | — |
| ITGA6 | 0.828 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=67.5 + PDB: 3GJO, 7OLG | pLDDT=67.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton,  / Nucleoplasm, Microtubules; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DST — Dystonin，有一定研究基础，但仍存在niche空间。
2. 蛋白大小7570 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 598 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 598 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q03001
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151914-DST/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DST
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q03001
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:20:13

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000151914-DST/subcellular

![](https://images.proteinatlas.org/30200/319_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/30200/319_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/30200/320_F8_3_red_green.jpg)
![](https://images.proteinatlas.org/30200/320_F8_4_red_green.jpg)
![](https://images.proteinatlas.org/30200/340_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/30200/340_F8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q03001 |
| SMART | SM00033;SM00054;SM00243;SM00250;SM00150; |
| UniProt Domain [FT] | DOMAIN 35..138; /note="Calponin-homology (CH) 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00044"; DOMAIN 151..255; /note="Calponin-homology (CH) 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00044"; DOMAIN 887..944; /note="SH3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192"; DOMAIN 7197..7232; /note="EF-hand 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 7233..7268; /note="EF-hand 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 7273..7351; /note="GAR"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00792" |
| InterPro | IPR001589;IPR001715;IPR036872;IPR041615;IPR041573;IPR011992;IPR018247;IPR002048;IPR003108;IPR036534;IPR049538;IPR043197;IPR035915;IPR001101;IPR001452;IPR018159;IPR002017; |
| Pfam | PF00307;PF13499;PF02187;PF00681;PF17902;PF00435;PF18373;PF21019;PF21020;PF21097; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000151914-DST/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APPL1 | Intact, Biogrid | true |
| MAPRE1 | Intact, Biogrid | true |
| OPTN | Intact, Biogrid | true |
| ACTB | Biogrid | false |
| ANLN | Biogrid | false |
| BMI1 | Biogrid | false |
| COL17A1 | Biogrid | false |
| DCTN1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
