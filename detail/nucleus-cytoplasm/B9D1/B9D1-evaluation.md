---
type: protein-evaluation
gene: "B9D1"
date: 2026-06-03
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## B9D1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | B9D1 / MKSR1 |
| 蛋白全名 | B9 domain-containing protein 1 |
| 蛋白大小 | 204 aa / 22.8 kDa |
| UniProt ID | Q9UPM9 (B9D1_HUMAN) |
| 功能描述 | Component of the tectonic-like complex, a complex localized at the transition zone of primary cilia and acting as a barrier that prevents diffusion of transmembrane proteins between the cilia and plasma membranes. Required for ciliogenesis and sonic hedgehog/SHH signaling (By similarity) |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | HPA main: nucleoplasm, acrosome, equatorial segment, mid piece |
| 蛋白大小 | 6/10 | x1 | 6.0 | 204 aa / 22.8 kDa, <300或>800 |
| 研究新颖性 | 8/10 | x5 | 40.0 | PubMed strict=21（低研究量，21-40→8分） |
| 三维结构 | 6/10 | x3 | 18.0 | AF moderate-high: mean pLDDT 82.7 |
| 调控结构域 | 3/10 | x2 | 6.0 | No clear regulatory domain identified |
| PPI 网络 | 3/10 | x3 | 9.0 | IntAct experiment: 15 partners (1 regulatory: RB) |
| 互证加分 | — | — | +0.0 | 无 |
| **加权总分** | | | **99/180**************** | |
| **归一化总分 (÷1.83)** | | | **54.1/100**************** | |

### 3. HPA 免疫荧光分析

| HPA 主定位 | Nucleoplasm, Acrosome, Equatorial segment, Mid piece |
| HPA 额外定位 | Vesicles, Basal body, Cytosol, Principal piece, End piece |
| 抗体可靠性 | Uncertain |
| IF 图像 | IF images available (8 cell lines) |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 4. PubMed 文献

| strict (Title/Abstract + gene/protein) | 21 |
| symbol_only (Title/Abstract) | 27 |
| broad (all fields) | 27 |

1. PMID 20301500: Adam MP, Bick S, Mirzaa GM (1993). "Joubert Syndrome.." **.
2. PMID 21763481: Dowdle WE, Robinson JF, Kneist A (2011 Jul 15). "Disruption of a ciliary B9 protein complex causes Meckel syndrome.." *American journal of human genetics*.
3. PMID 40565534: Campobasso G, Mercuri L, De Razza F (2025 May 27). "Investigating the Role of B9D1 in Meckel-Gruber Syndrome: A Case Report and Comprehensive Literature Review.." *Genes*.
4. PMID 25869670: Roberson EC, Dowdle WE, Ozanturk A (2015 Apr 13). "TMEM231, mutated in orofaciodigital and Meckel syndromes, organizes the ciliary transition zone.." *The Journal of cell biology*.
5. PMID 41165761: He R, Li Y, Jin M (2026 Jan 16). "Ciliopathy-related B9 protein complex regulates ciliary axonemal microtubule posttranslational modifications and initiation of ciliogenesis.." *The Journal of clinical investigation*.

### 5. AlphaFold 结构预测

| 平均 pLDDT | 82.7 |
| pLDDT >90 | 58.8% |
| pLDDT 70-90 | 12.7% |
| pLDDT 50-70 | 24.0% |
| pLDDT <50 | 4.4% |

**评价**: AlphaFold 预测整体置信度较高（mean pLDDT 82.7），大部分区域折叠良好。



### 6. PDB 条目

0 entries found.

### 7. InterPro/Pfam 结构域

| InterPro | IPR010796 | IPR entry IPR010796 |
| Pfam | PF07162 | Pfam entry PF07162 |

**评价**: B9D1 是 transition zone 纤毛蛋白，在纤毛基部的过渡区形成扩散屏障，调控纤毛信号传导。

### 8. PPI 网络

#### STRING Top 10

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|---|
| TCTN1 | 0.999 | 0.572 | 0.800 | 0.990 |
| B9D2 | 0.999 | 0.882 | 0.800 | 0.959 |
| TMEM231 | 0.998 | 0.719 | 0.720 | 0.978 |
| CC2D2A | 0.998 | 0.233 | 0.800 | 0.989 |
| TMEM67 | 0.997 | 0.000 | 0.800 | 0.986 |
| TCTN2 | 0.997 | 0.363 | 0.800 | 0.982 |
| TMEM216 | 0.995 | 0.000 | 0.800 | 0.979 |
| TCTN3 | 0.993 | 0.071 | 0.800 | 0.968 |
| MKS1 | 0.993 | 0.556 | 0.800 | 0.930 |
| CEP290 | 0.987 | 0.000 | 0.720 | 0.954 |

#### IntAct Top 10

| Partner | Method | PMID | Interaction |
|---|---|---|---|
| Mks1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 | psi-mi:"MI:0914"(association) |
| rb | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 | psi-mi:"MI:0915"(physical association) |
| mRpS35 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 | psi-mi:"MI:0915"(physical association) |
| MED19 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 | psi-mi:"MI:0915"(physical association) |
| Hn | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 | psi-mi:"MI:0915"(physical association) |
| tctn | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 | psi-mi:"MI:0915"(physical association) |
| TMEM231 | psi-mi:"MI:2222"(inference by socio-affinity scoring) | pubmed:unassigned1312 | psi-mi:"MI:0915"(physical association) |
| B9D2 | psi-mi:"MI:2222"(inference by socio-affinity scoring) | pubmed:unassigned1312 | psi-mi:"MI:0915"(physical association) |
| POSTN | psi-mi:"MI:2222"(inference by socio-affinity scoring) | pubmed:unassigned1312 | psi-mi:"MI:0915"(physical association) |
| EXOSC10 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 | psi-mi:"MI:0915"(physical association) |

#### UniProt 互作

| Partner | Experiments |
|---|---|
| B9D2 | 10 |
| MKS1 | 4 |
| TMEM231 | 4 |

### 9. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 综合评分一般，多维度均未显示突出优势

**风险/不确定性**:
1. 核定位证据偏弱（得分 5/10），需要更多的实验验证

**分类**: nucleus-cytoplasm
**综合评分**: 54/100

---

**数据来源**: UniProt Q9UPM9, HPA ENSG00000108641, AlphaFold AF-Q9UPM9-F1, STRING, IntAct

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000108641-B9D1/subcellular

![](https://images.proteinatlas.org/22957/2124_G9_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/22957/2124_G9_30_blue_red_green.jpg)
![](https://images.proteinatlas.org/22957/2129_C4_59_blue_red_green.jpg)
![](https://images.proteinatlas.org/22957/2129_C4_78_blue_red_green.jpg)
![](https://images.proteinatlas.org/22957/2167_H3_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/22957/2167_H3_64_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPM9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UPM9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 9..127; /note="C2 B9-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00713" |
| InterPro | IPR010796; |
| Pfam | PF07162; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000108641-B9D1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| B9D2 | Intact, Biogrid, Bioplex | true |
| MKS1 | Intact, Biogrid | true |
| TMEM231 | Intact, Biogrid, Bioplex | true |
| TCTN2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
