---
type: protein-evaluation
gene: "COQ9"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COQ9 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=102，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COQ9 / C16orf49 |
| 蛋白名称 | Ubiquinone biosynthesis protein COQ9, mitochondrial |
| 蛋白大小 | 318 aa / 35.5 kDa |
| UniProt ID | O75208 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria, Cytosol; UniProt: Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 318 aa / 35.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=102 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.6; PDB: 4RHP, 6AWL, 6DEW, 7SSP, 7SSS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013718, IPR048674, IPR012762; Pfam: PF08511, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **74.0/180** | |
| **归一化总分** | | | **41.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria, Cytosol | Approved |
| UniProt | Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)
- ubiquinone biosynthesis complex (GO:0110142)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 102 |
| PubMed broad count | 265 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf49 |

**关键文献**:
1. Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview.. **. PMID: 26425749
2. Coenzyme Q headgroup intermediates can ameliorate a mitochondrial encephalopathy.. *Nature*. PMID: 40634618
3. Design of CoQ(10) crops based on evolutionary history.. *Cell*. PMID: 39952246
4. Primary Coenzyme Q(10) Deficiency Overview.. **. PMID: 28125198
5. New variants expand the neurological phenotype of COQ7 deficiency.. *Journal of inherited metabolic disease*. PMID: 38973597

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.6 |
| 高置信度残基 (pLDDT>90) 占比 | 55.7% |
| 置信残基 (pLDDT 70-90) 占比 | 11.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 27.0% |
| 有序区域 (pLDDT>70) 占比 | 67.3% |
| 可用 PDB 条目 | 4RHP, 6AWL, 6DEW, 7SSP, 7SSS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4RHP, 6AWL, 6DEW, 7SSP, 7SSS）+ AlphaFold极高置信度预测（pLDDT=77.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013718, IPR048674, IPR012762; Pfam: PF08511, PF21392 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COQ7 | 0.999 | 0.937 | — |
| COQ3 | 0.996 | 0.434 | — |
| COQ5 | 0.993 | 0.395 | — |
| COQ8A | 0.991 | 0.427 | — |
| COQ6 | 0.990 | 0.467 | — |
| COQ4 | 0.986 | 0.466 | — |
| PDSS1 | 0.985 | 0.000 | — |
| COQ2 | 0.984 | 0.000 | — |
| PDSS2 | 0.971 | 0.000 | — |
| COQ8B | 0.947 | 0.436 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACTL6B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ANO8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NAF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| Dmel\CG9757 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| HSP78 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| tkv | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| XPNPEP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.6 + PDB: 4RHP, 6AWL, 6DEW, 7SSP, 7SSS | pLDDT=77.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion / Mitochondria, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. COQ9 — Ubiquinone biosynthesis protein COQ9, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小318 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 102 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75208
- Protein Atlas: https://www.proteinatlas.org/ENSG00000088682-COQ9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COQ9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75208
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000088682-COQ9/subcellular

![](https://images.proteinatlas.org/40918/1912_F5_14_cr5c8b667d4a841_blue_red_green.jpg)
![](https://images.proteinatlas.org/40918/1912_F5_22_cr5c86329339784_blue_red_green.jpg)
![](https://images.proteinatlas.org/40918/502_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40918/502_A4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/40918/557_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40918/557_A4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75208-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
