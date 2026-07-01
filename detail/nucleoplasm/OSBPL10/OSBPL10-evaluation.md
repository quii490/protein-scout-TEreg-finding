---
type: protein-evaluation
gene: "OSBPL10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OSBPL10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OSBPL10 / ORP10, OSBP9 |
| 蛋白名称 | Oxysterol-binding protein-related protein 10 |
| 蛋白大小 | 764 aa / 84.0 kDa |
| UniProt ID | Q9BXB5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus, Plasma membrane; 额外: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 10/10 | ×1 | 10 | 764 aa / 84.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR041 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- transporter complex (GO:1990351)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ORP10, OSBP9 |

**关键文献**:
1. Evolutionary history of sickle-cell mutation: implications for global genetic medicine.. *Human molecular genetics*. PMID: 33461216
2. Single-Cell Analysis Combined with Mendelian Randomization Identifies Genes Associated with Prostate Cancer Cells.. *The world journal of men's health*. PMID: 40583027
3. The immune cells have complex causal regulation effects on cancers.. *International immunopharmacology*. PMID: 38710118
4. Comparison of the Mutational Profile between BCL2- and BCL6-Rearrangement Positive Follicular Lymphoma.. *The Journal of molecular diagnostics : JMD*. PMID: 40482882
5. OSBPL10, RXRA and lipid metabolism confer African-ancestry protection against dengue haemorrhagic fever in admixed Cubans.. *PLoS pathogens*. PMID: 28241052

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.3 |
| 高置信度残基 (pLDDT>90) 占比 | 44.9% |
| 置信残基 (pLDDT 70-90) 占比 | 21.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 27.9% |
| 有序区域 (pLDDT>70) 占比 | 66.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.3，有序区 66.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037239, IPR000648, IPR018494, IPR011993, IPR041680; Pfam: PF01237, PF15409 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| IKBKG | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| USP11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| MMP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| NIPSNAP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SAP18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CLINT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PGAM5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| ALDOA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SRRM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.3 + PDB: 无 | pLDDT=73.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / Golgi apparatus, Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. OSBPL10 — Oxysterol-binding protein-related protein 10，非常新颖，仅有少数基础研究。
2. 蛋白大小764 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| AP2B1 | BioGRID | 0 |
| ALDOA | BioGRID | 0 |
| BBS1 | BioGRID | 0 |
| GBAS | BioGRID | 0 |
| MMP2 | BioGRID | 0 |
| CUL1 | BioGRID | 0 |
| CLINT1 | BioGRID | 0 |
| KEAP1 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：OSBPL10（764 aa / 84.0 kDa, UniProt Q9BXB5）是多结构域脂质转运蛋白，具有模块化架构：N端PH结构域（SM00233, IPR018494, PF15409, UniProt FT: DOMAIN 74-171）和C端OSBP相关结构域（ORD, IPR041680, IPR000648, PF01237，覆盖~200-764区域）。PH结构域通过磷酸肌醇识别介导膜靶向，ORD结构域包含氧化固醇结合口袋。AlphaFold v6中等置信度（pLDDT=73.3，44.9%残基>90，有序区66.4%）预测PH和ORD为独立折叠模块，通过长柔性linker连接——OSBP家族典型排列。较低pLDDT归因于域间柔性（~100残基linker区域）和部分未折叠区段，而各独立结构域可能折叠良好。IPR037239（OSBP超家族）和IPR011993（PH-like超家族）表明OSBPL10属于具有共同结构架构的大型脂质转运蛋白家族。

**PPI网络分析**：PPI画像独特：尽管存在15个IntAct互作，STRING预测伙伴为0（combined score阈值>0.4）。IntAct伙伴功能多样：IKBKG（NF-kappa-B必需调节因子，PMID:21988832）连接OSBPL10至炎症信号；USP11（去泛素酶）和MMP2（基质金属蛋白酶）暗示蛋白周转和细胞外基质重塑关联；SAP18（Sin3A相关蛋白18）是SIN3-HDAC辅抑制复合物和ASAP（凋亡/剪接相关蛋白）复合物的关键组分；SRRM2（丝氨酸/精氨酸重复基质蛋白2）为剪接体组分和核散斑marker；CLINT1（网格蛋白互作因子）与膜运输关联；PGAM5（线粒体磷酸酶）和ALDOA（糖酵解酶）扩展代谢-信号互作面。humanPPI数据（VAPA, VAPB, Biogrid/Opencell）确认OSBPL10与VAP蛋白的膜接触位点功能。SAP18互作最具机制意义——SAP18将SIN3复合物直接桥接至HDAC1/2，可能将OSBPL10的脂质转运活性招募至染色质调控复合物。

**结构解读与机制模型**：OSBPL10的主要机制围绕膜接触位点的非囊泡脂质转运。PH结构域靶向高尔基体（HPA: Golgi apparatus, approved）和质膜，ORD结构域在膜间转运氧化固醇（如25-羟基胆固醇）。氧化固醇是调控LXR转录因子、SREBP加工和炎症通路的强效信号脂质。OSBPL10的核质注释（HPA: Nucleoplasm, 非approved）可反映以下两种可能：要么是参与核脂质信号的真实核池，要么是高尔基体染色的污染/背景。SAP18和SRRM2互作（IntAct, PMID:19615732）提供分子桥梁至细胞核：若OSBPL10-SAP18共定位于核散斑，OSBPL10可将氧化固醇配体局部递送至核受体（LXRα/β），在特定亚核域调控转录。PH结构域的磷酸肌醇结合特异性（PIP种类偏好）决定了OSBPL10的亚细胞靶向，可能响应PI3K等信号通路动态调控。

**TE调控意义与实验建议**：OSBPL10与TE调控的关联为外围间接关系。LXR介导的氧化固醇信号与炎症基因调控关联，炎症是TE去抑制的已知触发因素。OSBPL10可能通过调节核氧化固醇浓度间接影响LXR依赖的转录程序，进而影响TE表达。最有希望的研究方向是SAP18互作：若OSBPL10通过SAP18与SIN3-HDAC复合物功能互作，可将脂质信号栓系至TE位点的组蛋白去乙酰化。然而，鉴于核定位信号弱（高尔基体>核质）和间接机制特征，OSBPL10应视为较低优先级的TE候选。验证优先级：（1）western blot确认核分级的OSBPL10定位；（2）co-IP SAP18并评估SIN3复合物招募；（3）氧化固醇处理对TE RNA表达的影响测试；（4）OSBPL10敲低后重复元件家族的RNA-seq扰动检测。

### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXB5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144645-OSBPL10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OSBPL10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXB5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000144645-OSBPL10/subcellular

![](https://images.proteinatlas.org/3636/77_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3636/77_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3636/78_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3636/78_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/3636/92_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/3636/92_H2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BXB5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BXB5 |
| SMART | SM00233; |
| UniProt Domain [FT] | DOMAIN 74..171; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145" |
| InterPro | IPR037239;IPR000648;IPR018494;IPR011993;IPR041680;IPR001849; |
| Pfam | PF01237;PF15409; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144645-OSBPL10/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| VAPA | Biogrid, Opencell | true |
| VAPB | Biogrid, Opencell | true |
| EEF1AKMT3 | Bioplex | false |
| HSPB8 | Bioplex | false |
| KCNE3 | Bioplex | false |
| OSBPL11 | Opencell | false |
| OSBPL9 | Intact | false |
| UBXN6 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
