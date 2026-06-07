---
type: protein-evaluation
gene: "TOX"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TOX — REJECTED (研究热度过高 (PubMed strict=1004，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TOX / KIAA0808 |
| 蛋白名称 | Thymocyte selection-associated high mobility group box protein TOX |
| 蛋白大小 | 526 aa / 57.5 kDa |
| UniProt ID | O94900 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli fibrillar center; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 526 aa / 57.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1004 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009071, IPR036910, IPR051365; Pfam: PF00505 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1004 |
| PubMed broad count | 7851 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0808 |

**关键文献**:
1. TOX is expressed by exhausted and polyfunctional human effector memory CD8(+) T cells.. *Science immunology*. PMID: 32620560
2. TOX reinforces the phenotype and longevity of exhausted T cells in chronic viral infection.. *Nature*. PMID: 31207605
3. Single-cell RNA-seq reveals TOX as a key regulator of CD8(+) T cell persistence in chronic infection.. *Nature immunology*. PMID: 31209400
4. Continuous expression of TOX safeguards exhausted CD8 T cell epigenetic fate.. *Science immunology*. PMID: 40053604
5. Spatial and functional targeting of intratumoral Tregs reverses CD8+ T cell exhaustion and promotes cancer immunotherapy.. *The Journal of clinical investigation*. PMID: 38787791

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.4 |
| 高置信度残基 (pLDDT>90) 占比 | 12.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 23.4% |
| 低置信 (pLDDT<50) 占比 | 58.9% |
| 有序区域 (pLDDT>70) 占比 | 17.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.4），有序残基占 17.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009071, IPR036910, IPR051365; Pfam: PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD5 | 0.606 | 0.000 | — |
| CD8A | 0.600 | 0.000 | — |
| TOX2 | 0.559 | 0.501 | — |
| CD4 | 0.546 | 0.066 | — |
| EOMES | 0.473 | 0.045 | — |
| NFIL3 | 0.459 | 0.000 | — |
| TBX21 | 0.442 | 0.052 | — |
| TSPAN7 | 0.440 | 0.000 | — |
| TCF7 | 0.437 | 0.000 | — |
| ZBTB7B | 0.435 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRAP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRTAP26-1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DMRTB1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BANP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TOX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KRTAP12-1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-21827|pubmed:24705354 |
| KLK6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| MYH9 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ALDH16A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.4 + PDB: 无 | pLDDT=54.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TOX — Thymocyte selection-associated high mobility group box protein TOX，研究基础较多，新颖性有限。
2. 蛋白大小526 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1004 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=54.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1004 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94900
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198846-TOX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TOX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94900
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000198846-TOX/subcellular

![](https://images.proteinatlas.org/73241/1398_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/73241/1398_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/73241/1403_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/73241/1403_F5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94900-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O94900 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009071;IPR036910;IPR051365; |
| Pfam | PF00505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198846-TOX/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DMRTB1 | Intact | false |
| GRAP | Intact | false |
| KLK6 | Intact | false |
| KRTAP12-1 | Intact | false |
| KRTAP26-1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
