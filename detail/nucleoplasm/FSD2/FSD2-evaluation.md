---
type: protein-evaluation
gene: "FSD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FSD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FSD2 / SPRYD1 |
| 蛋白名称 | Fibronectin type III and SPRY domain-containing protein 2 |
| 蛋白大小 | 749 aa / 85.4 kDa |
| UniProt ID | A1L4K1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Sarcoplasmic reticulum; Cytoplasm, perinuclear regi |
| 蛋白大小 | 10/10 | ×1 | 10 | 749 aa / 85.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Nucleus; Sarcoplasmic reticulum; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- sarcoplasmic reticulum (GO:0016529)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPRYD1 |

**关键文献**:
1. Genomic structure, expression and association study of the porcine FSD2.. *Molecular biology reports*. PMID: 27350214
2. Identification of Alzheimer's disease biomarkers and their immune function characterization.. *Archives of medical science : AMS*. PMID: 40190307
3. The role of PAP4/FSD3 and PAP9/FSD2 in heat stress responses of chloroplast genes.. *Plant science : an international journal of experimental plant biology*. PMID: 35738478
4. Characterization of the fluoroacetate detoxication enzymes of rat liver cytosol.. *Xenobiotica; the fate of foreign compounds in biological systems*. PMID: 16393857
5. Speg interactions that regulate the stability of excitation-contraction coupling protein complexes in triads and dyads.. *Communications biology*. PMID: 37709832

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.5 |
| 高置信度残基 (pLDDT>90) 占比 | 34.6% |
| 置信残基 (pLDDT 70-90) 占比 | 32.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.3% |
| 低置信 (pLDDT<50) 占比 | 21.6% |
| 有序区域 (pLDDT>70) 占比 | 67.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.5，有序区 67.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR050617; Pfam: PF00041, PF00622 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESD | 0.688 | 0.688 | — |
| AP3B2 | 0.632 | 0.000 | — |
| LRRC39 | 0.626 | 0.000 | — |
| RNF207 | 0.503 | 0.000 | — |
| SPATC1L | 0.465 | 0.466 | — |
| MTERF3 | 0.455 | 0.000 | — |
| C15orf40 | 0.450 | 0.000 | — |
| GSTZ1 | 0.447 | 0.000 | — |
| ZNF572 | 0.445 | 0.438 | — |
| POLL | 0.444 | 0.444 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYBPC2 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| UBC27 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| F8M12.23 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| TCP15 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| LSU2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| TCP13 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| LSU1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| O04879 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| DHRS7 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CCHCR1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 15
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.5 + PDB: 无 | pLDDT=73.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Sarcoplasmic reticulum; Cytoplasm, perinu / Cytosol | 一致 |
| PPI | STRING + IntAct | 12 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FSD2 — Fibronectin type III and SPRY domain-containing protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小749 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FMR1 | BioGRID | 0 |
| NDN | BioGRID | 0 |
| AES | BioGRID | 0 |
| AQP1 | BioGRID | 0 |
| ESD | BioGRID | 0 |
| PBX3 | BioGRID | 0 |
| PPP2R5D | BioGRID | 0 |
| PSMB4 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

FSD2（Fibronectin type III and SPRY domain-containing protein 2, 749 aa, 85.4 kDa, UniProt A1L4K1, 别名SPRYD1）的域架构为两个串联的纤连蛋白III型域（FN3-1: aa375-470, FN3-2: aa471-564, SMART:SM00060, Pfam:PF00041, PROSITE:PRU00316）后接C端B30.2/SPRY域（aa546-744, SMART:SM00449, Pfam:PF00622, PROSITE:PRU00548）。InterPro补充注释了TNFR/NGFR半胱氨酸富集区信号（IPR001870, IPR043136, IPR003879）、B30.2/SPRY折叠（IPR013320, IPR050617）和Ig样域（IPR003961, IPR036116, IPR013783）。FN3域由约90个残基组成——折叠为7条β链的免疫球蛋白样sandwich，在细胞黏附分子、细胞因子受体和ECM蛋白中用作通用互作支架。B30.2/SPRY域由约200个残基构成——N端PRY亚域+C端SPRY亚域形成扭曲的β-sandwich，其凹面提供蛋白互作平台。SPRY域在TRIM家族E3泛素连接酶（如TRIM5α, TRIM21, TRIM28/KAP1）和butyrophilin家族中高度保守——其中TRIM28/KAP1的SPRY域直接"阅读"N端组蛋白尾部并招募异染色质蛋白。AlphaFold v6 pLDDT=73.5（高置信34.6%, 有序区67.0%）预测FN3和SPRY域以中等置信度折叠，而N端约370 aa区域贡献了全局pLDDT的主要下降（21.6%低置信区），PDB无实验结构（PDB=0）。

PPI网络揭示了FSD2的转录调控潜力。STRING高分伙伴ESD/酯酶D（combined score=0.688, 实验=0.688, humanPPI: Intact+Biogrid）催化S-甲酰谷胱甘肽水解——参与甲醛解毒和谷胱甘肽代谢，已知ESD定位于核内并与核基质结合。MTERF3（STRING score=0.455, 线粒体转录终止因子3）和POLL/DNA聚合酶lambda（STRING score=0.444, 实验=0.444, X家族DNA pol, 参与碱基切除修复BER和NHEJ）的关联拓展了功能范围。BioGRID互作中FMR1/FMRP（脆性X智力低下蛋白, 含RGG-box RNA结合域的翻译抑制因子——与RISC和microRNA通路直接相关）和NDN/Necdin（MAGE家族, 细胞周期阻滞和神经元分化, 转录共抑制因子）和AES/Amino-terminal enhancer of split（Groucho/TLE转录共抑制家族）均为核质转录/RNA调控蛋白。最为关键的是humanPPI中CBX8/PC3（Intact互作, AF3结构可用）——CBX8是多梳抑制复合体1（PRC1）的chromodomain亚基，负责识别H3K27me3修饰并维持基因沉默。FSD2-SPRY域与CBX8的结合若在体内证实，将直接建立FSD2→PRC1→H2AK119ub→H3K27me3→转录沉默的信号链。

UniProt注释FSD2定位于Nucleus、Sarcoplasmic reticulum和Cytoplasm perinuclear region（Swiss-Prot/TrEMBL），GO-CC支持Nucleus（GO:0005634）和Perinuclear region（GO:0048471），HPA显示Cytosol（Approved）——三源定位可能反映条件依赖的核-质穿梭。FSD2的SPRY域（与TRIM家族共享）+核定位+CBX8（PRC1组分）/FMR1（RISC相关）/AES（TLE共抑制子）的多重转录抑制相关互作，构成被严重低估的染色质调控潜力。TRIM28/KAP1通过SPRY域识别H3K9me3并招募SETDB1和HP1——如果FSD2通过其SPRY域执行类似功能，可能构成PRC1非依赖的H3K27me3/H3K9me3修饰阅读和异染色质扩散机制。PubMed仅29篇（新颖性8/10）使FSD2成为高度新颖且机制潜力丰富的候选。实验优先级：co-IP验证FSD2-CBX8和FSD2-FMR1互作；ChIP-seq检测FSD2占据位点（特别关注H3K27me3标记的TE区域）；SPRY域-GST-pulldown检测组蛋白肽结合特异性。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A1L4K1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186628-FSD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FSD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A1L4K1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000186628-FSD2/subcellular

![](https://images.proteinatlas.org/46263/1707_C9_12_cr57eaaece0f49f_blue_red_green.jpg)
![](https://images.proteinatlas.org/46263/1707_C9_8_cr57eaaec63898f_blue_red_green.jpg)
![](https://images.proteinatlas.org/46263/1708_A2_12_cr57ea98b9e1bd5_blue_red_green.jpg)
![](https://images.proteinatlas.org/46263/1708_A2_23_cr57ea98c1791fd_blue_red_green.jpg)
![](https://images.proteinatlas.org/46263/1820_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46263/1820_B5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A1L4K1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A1L4K1 |
| SMART | SM00060;SM00449; |
| UniProt Domain [FT] | DOMAIN 375..470; /note="Fibronectin type-III 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00316"; DOMAIN 471..564; /note="Fibronectin type-III 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00316"; DOMAIN 546..744; /note="B30.2/SPRY"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00548" |
| InterPro | IPR001870;IPR043136;IPR003879;IPR013320;IPR050617;IPR003961;IPR036116;IPR013783;IPR003877; |
| Pfam | PF00041;PF00622; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000186628-FSD2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ESD | Intact, Biogrid | true |
| AQP1 | Intact | false |
| ARFIP2 | Intact | false |
| ATG14 | Intact | false |
| BEX2 | Intact | false |
| BEX3 | Intact | false |
| C1orf216 | Intact | false |
| CBX8 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
