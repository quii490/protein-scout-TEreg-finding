---
type: protein-evaluation
gene: "GPKOW"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPKOW 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPKOW / GPATC5, GPATCH5, T54 |
| 蛋白名称 | G-patch domain and KOW motifs-containing protein |
| 蛋白大小 | 476 aa / 52.2 kDa |
| UniProt ID | Q92917 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 476 aa / 52.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.7; PDB: 7DVQ, 7QTT, 8CH6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000467, IPR041993, IPR041994, IPR005824, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.5/180** | |
| **归一化总分** | | | **77.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spliceosomal complex (GO:0005681)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GPATC5, GPATCH5, T54 |

**关键文献**:
1. Protein turnover regulation is critical for influenza A virus infection.. *Cell systems*. PMID: 39368468
2. C-terminal frameshift variants in GPKOW are associated with a multisystemic X-linked disorder.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 40221893
3. Variant in the X-chromosome spliceosomal gene GPKOW causes male-lethal microcephaly with intrauterine growth restriction.. *European journal of human genetics : EJHG*. PMID: 28612833
4. G-patch domain and KOW motifs-containing protein, GPKOW; a nuclear RNA-binding protein regulated by protein kinase A.. *Journal of molecular signaling*. PMID: 21880142
5. GPKOW is essential for pre-mRNA splicing in vitro and suppresses splicing defect caused by dominant-negative DHX16 mutation in vivo.. *Bioscience reports*. PMID: 25296192

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.7 |
| 高置信度残基 (pLDDT>90) 占比 | 23.5% |
| 置信残基 (pLDDT 70-90) 占比 | 31.3% |
| 中等置信 (pLDDT 50-70) 占比 | 15.5% |
| 低置信 (pLDDT<50) 占比 | 29.6% |
| 有序区域 (pLDDT>70) 占比 | 54.8% |
| 可用 PDB 条目 | 7DVQ, 7QTT, 8CH6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.7），有序残基占 54.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000467, IPR041993, IPR041994, IPR005824, IPR014722; Pfam: PF12656, PF25088, PF00467 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DHX16 | 0.999 | 0.998 | — |
| DHX38 | 0.998 | 0.994 | — |
| RBM10 | 0.996 | 0.994 | — |
| BUD13 | 0.983 | 0.965 | — |
| RNF113A | 0.971 | 0.800 | — |
| CWC27 | 0.971 | 0.802 | — |
| CWC22 | 0.968 | 0.800 | — |
| PPIL2 | 0.962 | 0.802 | — |
| PRPF8 | 0.957 | 0.936 | — |
| ARMC7 | 0.936 | 0.922 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NINL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| hdlbp.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| Bud13 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| HNRNPC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| GOLGA2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TRAF2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TCEA2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TRIM23 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.7 + PDB: 7DVQ, 7QTT, 8CH6 | pLDDT=69.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GPKOW — G-patch domain and KOW motifs-containing protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小476 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DHX16 | STRING | 999 |
| DHX38 | STRING | 998 |
| RBM10 | STRING | 996 |
| BUD13 | STRING | 983 |
| RNF113A | STRING | 971 |
| CWC27 | STRING | 971 |
| CWC22 | STRING | 968 |
| PPIL2 | STRING | 962 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

GPKOW（UniProt Q92917）是剪接体中一个多功能RNA结合蛋白，其结构域架构包含一个N端G-patch结构域（SMART:SM00443，残基164-210）和两个C端KOW基序（KOW1: 240-267, KOW2: 415-442），中间由一段低置信度连接区隔开。G-patch结构域是RNA解旋酶激活模块，已知通过与DHX16等DEAH-box RNA解旋酶的相互作用促进剪接体重塑（PMID:25296192）；KOW基序则是古老的核糖体蛋白折叠，在真核生物中进化出核酸结合功能。AlphaFold v6预测的pLDDT平均值仅为69.7，有序区域仅占54.8%，高置信区域（pLDDT>90）仅23.5%——这种中等置信度结构特征与其天然折叠/无序动态平衡一致，反映GPKOW作为剪接体脚手架蛋白需要构象灵活性来适应多种互作伙伴。

STRING-PPI网络强烈支持GPKOW是剪接体功能核心蛋白：DHX16（0.999, experimental=0.998）、DHX38（0.998, 0.994）、RBM10（0.996, 0.994）、BUD13（0.983, 0.965）、PRPF8（0.957, 0.936）均为剪接体A/B/C复合体的核心组分。PDB结构（7DVQ、7QTT、8CH6）捕获了GPKOW片段在剪接体组装不同阶段的构象，确证其直接参与pre-mRNA剪接催化。IntAct实验也捕捉到GPKOW与核纤层蛋白LMNA（PMID:29568061，proximity-dependent biotin identification）和hnRNPC（PMID:30021884，cross-linking）的互作，暗示其与核基质及RNA加工网络的更广泛关联。

HPA免疫荧光将GPKOW定位于核质（nucleoplasm, enhanced），与UniProt的nucleus注释完全一致，GO进一步指向nucleoplasm（GO:0005654）和spliceosomal complex（GO:0005681），核定位证据极其充分。放射自显影和激酶实验确认GPKOW是PKA的直接磷酸化底物（PMID:21880142），磷酸化修饰调控其RNA结合活性。

与TE调控最相关的线索是：GPKOW为X连锁基因，其C端移码突变被新近发现导致多系统X连锁疾病，包括小头畸形和宫内生长受限（PMID:28612833, PMID:40221893）。这些神经发育表型与许多染色质重塑因子和TE调控蛋白的突变表型高度重叠。考虑到GPKOW在剪接体中的核心地位，其功能缺失可能通过pre-mRNA剪接异常影响TE衍生外显子和转座元件的正确剪接加工，间接调控TE表达。G-patch/KOW双模块结构赋予GPKOW作为剪接体RNA解旋酶活化和RNA底物识别的双重分子机制，但其对TE衍生序列的选择性结合能力有待CLIP-seq实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92917
- Protein Atlas: https://www.proteinatlas.org/ENSG00000068394-GPKOW/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPKOW
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92917
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000068394-GPKOW/subcellular

![](https://images.proteinatlas.org/1894/13_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/1894/13_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/1894/16_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/1894/16_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/1894/24_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/1894/24_G7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92917-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92917 |
| SMART | SM00443;SM00739; |
| UniProt Domain [FT] | DOMAIN 164..210; /note="G-patch"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00092"; DOMAIN 240..267; /note="KOW 1"; DOMAIN 415..442; /note="KOW 2" |
| InterPro | IPR000467;IPR041993;IPR041994;IPR005824;IPR014722;IPR045166;IPR026822; |
| Pfam | PF12656;PF25088;PF00467; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000068394-GPKOW/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BUD13 | Intact, Biogrid | true |
| DHX16 | Intact, Biogrid, Bioplex | true |
| DHX38 | Intact, Biogrid | true |
| PRPF4 | Intact, Biogrid | true |
| PRPF8 | Intact, Biogrid | true |
| RBM10 | Intact, Biogrid | true |
| TERF2IP | Intact, Biogrid | true |
| ZRANB1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
