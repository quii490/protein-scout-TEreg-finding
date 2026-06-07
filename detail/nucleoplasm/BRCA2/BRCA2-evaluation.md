---
type: protein-evaluation
gene: "BRCA2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BRCA2 — REJECTED (研究热度过高 (PubMed strict=6035，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRCA2 / FACD, FANCD1 |
| 蛋白名称 | Breast cancer type 2 susceptibility protein |
| 蛋白大小 | 3418 aa / 384.2 kDa |
| UniProt ID | P51587 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm, cytoskeleton, microtubule organizing cen |
| 蛋白大小 | 0/10 | ×1 | 0 | 3418 aa / 384.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=6035 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 1N0W, 3EU7, 6GY2, 6HQU, 7BDX, 7LDG, 8BR9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015525, IPR015252, IPR036315, IPR015187, IPR048 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65.0/180** | |
| **归一化总分** | | | **36.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- BRCA2-MAGE-D1 complex (GO:0033593)
- centrosome (GO:0005813)
- chromosome, telomeric region (GO:0000781)
- cytosol (GO:0005829)
- DNA repair complex (GO:1990391)
- lateral element (GO:0000800)
- nuclear ubiquitin ligase complex (GO:0000152)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6035 |
| PubMed broad count | 16935 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FACD, FANCD1 |

**关键文献**:
1. BRCA2 gene mutation in cancer.. *Medicine*. PMID: 36397405
2. The BRCA1 and BRCA2 Genes in Early-Onset Breast Cancer Patients.. *Advances in experimental medicine and biology*. PMID: 29687286
3. Strong functional data for pathogenicity or neutrality classify BRCA2 DNA-binding-domain variants of uncertain significance.. *American journal of human genetics*. PMID: 33609447
4. A glycolytic metabolite bypasses "two-hit" tumor suppression by BRCA2.. *Cell*. PMID: 38608703
5. Breast cancer risks associated with missense variants in breast cancer susceptibility genes.. *Genome medicine*. PMID: 35585550

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
| 可用 PDB 条目 | 1N0W, 3EU7, 6GY2, 6HQU, 7BDX, 7LDG, 8BR9, 8C3J, 8C3N, 8PBC |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015525, IPR015252, IPR036315, IPR015187, IPR048262; Pfam: PF09169, PF09103, PF09104 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SEM1 | 0.999 | 0.879 | — |
| RAD51 | 0.999 | 0.996 | — |
| PALB2 | 0.999 | 0.997 | — |
| BARD1 | 0.999 | 0.793 | — |
| FANCD2 | 0.999 | 0.842 | — |
| BRCA1 | 0.999 | 0.896 | — |
| RAD51C | 0.999 | 0.635 | — |
| XRCC3 | 0.999 | 0.886 | — |
| BRIP1 | 0.998 | 0.292 | — |
| BCCIP | 0.997 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| spn-A | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| FANCD2 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:15115758 |
| RAD51 | psi-mi:"MI:0018"(two hybrid) | pubmed:9560268 |
| ENSP00000505508.1 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:12442171 |
| SEM1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10373512 |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| RPA1 | psi-mi:"MI:0096"(pull down) | pubmed:12527904 |
| RPA2 | psi-mi:"MI:0096"(pull down) | pubmed:12527904 |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 1N0W, 3EU7, 6GY2, 6HQU, 7BDX,  | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, microtubule orga / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. BRCA2 — Breast cancer type 2 susceptibility protein，研究基础较多，新颖性有限。
2. 蛋白大小3418 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 6035 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 6035 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51587
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139618-BRCA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRCA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51587
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000139618-BRCA2/subcellular

![](https://images.proteinatlas.org/26815/218_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/26815/218_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/26815/219_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/26815/219_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/26815/220_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/26815/220_D7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P51587 |
| SMART | SM01341; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR015525;IPR015252;IPR036315;IPR015187;IPR048262;IPR015188;IPR002093;IPR055077;IPR012340;IPR015205; |
| Pfam | PF09169;PF09103;PF09104;PF00634;PF22687;PF21318;PF09121; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139618-BRCA2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BRCA1 | Intact, Biogrid | true |
| DMC1 | Intact, Biogrid | true |
| FANCD2 | Intact, Biogrid | true |
| HMG20B | Intact, Biogrid | true |
| PALB2 | Intact, Biogrid, Bioplex | true |
| PDS5B | Intact, Biogrid | true |
| POLH | Intact, Biogrid | true |
| RAD51 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
