---
type: protein-evaluation
gene: "CFLAR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CFLAR — REJECTED (研究热度过高 (PubMed strict=185，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CFLAR / CASH, CASP8AP1, CLARP, MRIT |
| 蛋白名称 | CASP8 and FADD-like apoptosis regulator |
| 蛋白大小 | 480 aa / 55.3 kDa |
| UniProt ID | O15519 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane, Cytosol; 额外: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 480 aa / 55.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=185 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.3; PDB: 2N5R, 3H11, 3H13, 6M6O, 7DEE, 7LXC, 8YBX |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029030, IPR011029, IPR001875, IPR011600, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.0/180** | |
| **归一化总分** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane, Cytosol; 额外: Nuclear bodies | Supported |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- CD95 death-inducing signaling complex (GO:0031265)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- death-inducing signaling complex (GO:0031264)
- ripoptosome (GO:0097342)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 185 |
| PubMed broad count | 1209 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CASH, CASP8AP1, CLARP, MRIT |

**关键文献**:
1. Decoding cell death signals in liver inflammation.. *Journal of hepatology*. PMID: 23567086
2. Silibinin ameliorates hepatic lipid accumulation and oxidative stress in mice with non-alcoholic steatohepatitis by regulating CFLAR-JNK pathway.. *Acta pharmaceutica Sinica. B*. PMID: 31384535
3. The interaction of CFLAR with p130Cas promotes cell migration.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 36400248
4. Caspase-8 activation by cigarette smoke induces pro-inflammatory cell death of human macrophages exposed to lipopolysaccharide.. *Cell death & disease*. PMID: 38007509
5. Targeting c-FLICE-like inhibitory protein (CFLAR) in cancer.. *Expert opinion on therapeutic targets*. PMID: 23252466

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.3 |
| 高置信度残基 (pLDDT>90) 占比 | 48.3% |
| 置信残基 (pLDDT 70-90) 占比 | 27.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 19.2% |
| 有序区域 (pLDDT>70) 占比 | 75.6% |
| 可用 PDB 条目 | 2N5R, 3H11, 3H13, 6M6O, 7DEE, 7LXC, 8YBX, 8YD7, 8YD8, 8YM4 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2N5R, 3H11, 3H13, 6M6O, 7DEE, 7LXC, 8YBX, 8YD7, 8YD8, 8YM4）+ AlphaFold极高置信度预测（pLDDT=78.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029030, IPR011029, IPR001875, IPR011600, IPR001309; Pfam: PF01335, PF00656 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FADD | 0.999 | 0.882 | — |
| CASP8 | 0.999 | 0.991 | — |
| TRADD | 0.999 | 0.045 | — |
| RIPK1 | 0.999 | 0.790 | — |
| CASP10 | 0.998 | 0.829 | — |
| FAS | 0.997 | 0.791 | — |
| ATG3 | 0.995 | 0.292 | — |
| ITCH | 0.992 | 0.839 | — |
| RIPK3 | 0.992 | 0.067 | — |
| TNFRSF10B | 0.991 | 0.797 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CASP8 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12887920 |
| CASP10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12887920 |
| USP15 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DOK2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RPS29 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SF3B3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| FBL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EPPK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| FSCN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SF3B1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.3 + PDB: 2N5R, 3H11, 3H13, 6M6O, 7DEE,  | pLDDT=78.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Plasma membrane, Cytosol; 额外: Nuclear | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CFLAR — CASP8 and FADD-like apoptosis regulator，研究基础较多，新颖性有限。
2. 蛋白大小480 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 185 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 185 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15519
- Protein Atlas: https://www.proteinatlas.org/ENSG00000003402-CFLAR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CFLAR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15519
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000003402-CFLAR/subcellular

![](https://images.proteinatlas.org/19044/115_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/19044/115_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/19044/116_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/19044/116_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/19044/117_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/19044/117_G10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15519-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15519 |
| SMART | SM00115;SM00031; |
| UniProt Domain [FT] | DOMAIN 1..73; /note="DED 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00065"; DOMAIN 92..170; /note="DED 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00065" |
| InterPro | IPR029030;IPR011029;IPR001875;IPR011600;IPR001309;IPR015917; |
| Pfam | PF01335;PF00656; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000003402-CFLAR/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CASP10 | Intact, Biogrid | true |
| CASP8 | Intact, Biogrid | true |
| TRAF1 | Intact, Biogrid | true |
| BIRC3 | Biogrid | false |
| CASP3 | Biogrid | false |
| CUL1 | Biogrid | false |
| DEDD | Biogrid | false |
| DEDD2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
