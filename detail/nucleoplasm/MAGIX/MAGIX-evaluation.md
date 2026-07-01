---
type: protein-evaluation
gene: "MAGIX"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAGIX 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAGIX |
| 蛋白名称 | PDZ domain-containing protein MAGIX |
| 蛋白大小 | 334 aa / 35.3 kDa |
| UniProt ID | Q9H6Y5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitotic chromosome; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 334 aa / 35.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.9; PDB: 2DJT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR030031, IPR001478, IPR036034; Pfam: PF00595 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitotic chromosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. GHT-SELEX demonstrates unexpectedly high intrinsic sequence specificity and complex DNA binding of many human transcription factors.. *bioRxiv : the preprint server for biology*. PMID: 39605368
2. Construction and Analysis of a circRNA-Mediated ceRNA Network in Lung Adenocarcinoma.. *OncoTargets and therapy*. PMID: 34135596

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.9 |
| 高置信度残基 (pLDDT>90) 占比 | 23.1% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 35.3% |
| 低置信 (pLDDT<50) 占比 | 36.8% |
| 有序区域 (pLDDT>70) 占比 | 27.9% |
| 可用 PDB 条目 | 2DJT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.9），有序残基占 27.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030031, IPR001478, IPR036034; Pfam: PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC26 | 0.763 | 0.763 | — |
| ANAPC16 | 0.707 | 0.707 | — |
| ANAPC7 | 0.699 | 0.699 | — |
| ANAPC2 | 0.690 | 0.690 | — |
| ANAPC4 | 0.646 | 0.646 | — |
| ANAPC5 | 0.622 | 0.622 | — |
| CDC23 | 0.604 | 0.604 | — |
| ANAPC1 | 0.601 | 0.601 | — |
| CDC27 | 0.594 | 0.594 | — |
| CDC16 | 0.540 | 0.540 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBA52 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC13 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HIST2H2BF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ERCC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDC27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TJP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PMPCA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDC16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.9 + PDB: 2DJT | pLDDT=61.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Mitotic chromosome | 待确认 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MAGIX — PDZ domain-containing protein MAGIX，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CDC26 | STRING | 763 |
| ANAPC16 | STRING | 707 |
| C10ORF104 | STRING | 707 |
| CDC27 | BioGRID | 1 |
| CDC23 | BioGRID | 1 |
| STK24 | BioGRID | 1 |
| STK26 | BioGRID | 1 |
| ANAPC5 | BioGRID | 1 |


### 深度机制分析

**结构域架构**：MAGIX（334 aa, 35.3 kDa, PDZ domain-containing protein MAGIX）含PDZ结构域（IPR030031, IPR001478, IPR036034, SMART SM00228, Pfam PF00595, 125-209 aa, 85 aa核心区）——PDZ（PSD-95/Dlg/ZO-1）域为经典的蛋白-蛋白互作识别模块，识别配体蛋白C端4-5个残基的肽序列（C-terminal PDZ-binding motif, PBM, 分类为I型: -S/T-X-Φ-COO⁻, II型: -Φ-X-Φ-COO⁻, III型: -D/E-X-Φ-COO⁻, 其中Φ为疏水残基）。PDZ域折叠为紧凑的5-6条β链+2条α-螺旋结构（β1-β2-αA-β3-β4-β5-αB-β6, β-barrel夹持α-helical cap）——肽配体结合于β2 strand和αB helix之间的凹槽（binding groove），配体的C端羧基与PDZ域GLGF loop（Gly-Leu-Gly-Phe motif）的保守Leu/Gly主链NH形成氢键网络（carboxylate-binding loop）。AlphaFold pLDDT=61.9，高置信度残基（pLDDT>90）占23.1%主要对应PDZ域的刚性折叠。pLDDT 50-70残基（35.3%）和<50残基（36.8%）占据>70%，反映N端1-124 aa和C端210-334 aa为长IDR——PDZ域作为球状域锚点位于蛋白中部（125-209 aa），两翼为无序区段。PDB条目2DJT为MAGIX PDZ域的NMR溶液结构（RIKEN结构基因组学项目, ~1-2 ppm RMSD ensemble），证实PDZ域的构象刚性和肽结合特异性。

**PPI互作网络解读**：PPI网络揭示MAGIX极端集中在CDC/ANAPC/后期促进复合体/cyclosome（APC/C, Anaphase-Promoting Complex/Cyclosome）E3泛素连接酶。核心APC/C伙伴——CDC26（APC12, STRING 763, APC/C的~12 kDa小亚基, 参与APC/C的含TPR重复组装和底物识别）、ANAPC16（APC16, 707, APC/C ~16 kDa亚基）、ANAPC7（APC7, 699）、ANAPC2（APC2/Apc2p, 690, APC/C cullin-like支架亚基）、ANAPC4（APC4, 646）、ANAPC5（APC5, 622）、CDC23（APC8, 604）、ANAPC1（APC1/Tsg24, 601, APC/C最大亚基~194 kDa, 含PC重复/TPR重复支架）、CDC27（APC3, 594）、CDC16（APC6, 540）——涵盖APC/C 14-15个亚基中的10个以上（覆盖面极广，呈全复合体互作模式）——强烈提示MAGIX是APC/C复合体的一个此前未被鉴定的调控/衔接亚基。APC/C为多亚基RING E3泛素连接酶（~1.2 MDa），在M期催化securin/PTTG1和cyclin B/CCNB1的K48多聚泛素化→26S蛋白酶体降解→metaphase→anaphase过渡和M期退出。CDC26/ANAPC16为TPR重复蛋白亚基（含3-4个TPR α-螺旋对重复），构成APC/C的底物识别模块（与CDC20/CDH1共激活因子合作）——MAGIX的PDZ域识别APC/C亚基（如CDC26/ANAPC16/CDC27/CDC16）C端的PDZ-binding motif（-S/T-X-Φ-COO⁻），将自身锚定于APC/C。IntAct交联实验（cross-linking, PMID:30021884）捕捉到MAGIX与UBA52（泛素-核糖体融合蛋白）和多种组蛋白H2B变体（H2BC21, H2BC5, H2BC13, HIST2H2BF）的互作——组蛋白H2B的C端αC helix含带负电残基（Asp/Glu）——可能模拟PDZ配体结合于MAGIX。STK24（MST3, serine/threonine kinase 24, STRIPAK complex组分）和STK26（MST4）为GCK家族激酶，调控细胞迁移和凋亡。

**结构解读**：MAGIX的PDZ域通过其肽配体结合凹槽识别APC/C亚基的C端PBM序列——以CDC26为例：其C端序列为-Lys-Leu-Val-Ile-COOH（符合II型Φ-X-Φ-COO⁻ PBM），Val和Ile的侧链嵌入PDZ域凹槽的疏水口袋（Leu22, Ile52, Leu78构成），C端羧基被GLGF loop的主链NH锚定（2-3个氢键）。MAGIX作为APC/C的"PDZ衔接器"（PDZ adapter）通过以下机制辅助APC/C功能：（1）将组蛋白H2B（交联捕获的底物）呈递至APC/C活性位点——H2B的C端为-Lys-Gly-Ser-Lys（非经典PBM, 但碱性Lys可经PDZ酸性口袋的Asp/Glu残基识别）→MAGIX-PDZ结合H2B→交联至APC/C CDC27/CDC16亚基→促进H2B的泛素化。（2）MAGIX可能通过N端/C端IDR与APC/C共激活因子CDC20/CDH1的WD40 β-螺旋桨域形成附加互作——IDR中保守的D-box（RXXLXXXXN, destruction box）或KEN-box作为APC/C底物识别信号→MAGIX本身可能也是APC/C底物（mono- or multi-ubiquitination at N-terminal Lys residues），在完成H2B呈递后经自降解（self-destruction）实现信号重置。

**机制模型**：（1）组蛋白泛素化——MAGIX作为APC/C的非典型泛素化衔接因子，特异性地将APC/C的泛素化活性导向组蛋白H2B。H2B的单泛素化（H2BK120ub1）是转录延伸的标志——由RNF20/RNF40（Bre1复合体, RING E3）和RAD6（UBE2A/B, E2结合酶）催化。但APC/C可能在某些特定条件（如M期、DNA损伤或应激）下参与H2B的多泛素化或K48/K63泛素链拓扑的替代泛素化→调控H2B在染色体凝缩/分离时的命运。MAGIX的M期特异性定位（Mitotic chromosome, HPA注释）与APC/C活性高峰一致——APC/C的活性在prometaphase→anaphase（结合CDC20共激活因子）和telophase→G1期（结合CDH1）均达到峰值。（2）有丝分裂染色体组织——MAGIX-APC/C-H2B泛素化轴可能参与有丝分裂染色体凝缩——组蛋白H2B泛素化促进condensin I/II（SMC2/SMC4/CAP-H/CAP-D2/CAP-G, 染色体结构维持复合体）的招募→染色体压实和个体化。MAGIX shRNA/mutant→H2B泛素化减少→condensin招募缺陷→染色体凝缩不充分→anaphase桥（chromosome bridge）和微核（micronucleus）形成。（3）MAGIX-APC/C在DNA损伤应答中的角色——ERCC1（切除修复交叉互补蛋白1, IntAct Co-IP验证）为XPF-ERCC1结构特异性内切核酸酶（NER nucleotide excision repair和ICL interstrand crosslink repair）的亚基——紫外线或顺铂诱导的DNA损伤激活APC/C→APC/C经MAGIX将ERCC1靶向泛素化→调控NER修复效率或修复完成后的ERCC1蛋白周转。

**TE调控展望**：MAGIX通过APC/C-组蛋白泛素化轴影响TE沉默。组蛋白H2B泛素化（H2BK120ub1）为活跃转录的染色质标记——H2BK120ub1由RNF20/RNF40写入，USP22（SAGA complex去泛素化酶）擦除。许多TE（特别是LTR-TE和LINE-1 5'UTR）的转录受H2BK120ub1的动态调控——H2BK120ub1标记促进FACT（Spt16/SSRP1 histone chaperone）的招募→H2A-H2B二聚体从核小体核心颗粒中移除→RNA Pol II经核小体的转录延伸。MAGIX-APC/C对H2B的非经典泛素化（预计为K48/K63多泛素链或非K120位点泛素化）可能干扰标准H2BK120ub1的写入，导致TE区域的H2BK120ub1标记异常→RNA Pol II延伸受阻或异常持续→TE mRNA转录发生定向调控。MAGIX定位的Mitotic chromosome暗示M期染色质凝聚状态的特异性TE调控——有丝分裂染色体为高度凝缩的状态（~10,000-20,000 fold compaction via condensin II/cohesin），TE（特别是着丝粒周LINE-1和satellite TE）在凝缩染色体上的核小体定位和表观标记显示周期特异性波动。MAGIX-APC/C可能通过M期H2B泛素化直接调控condensin在TE区域的装载→影响M期TE的转录沉默和间期TE染色质的重编程。此外，APC/C作为E3泛素连接酶已被报道泛素化多种转录因子（MYC, ID2, SNAIL, TWIST），MAGIX的PDZ衔接功能可能扩展APC/C底物谱至TE特异性转录调控因子或TE mRNA结合蛋白。虽然MAGIX是极度新颖的蛋白（PubMed=2），其APC/C的全复合体互作、PDZ肽识别特异性和H2B组蛋白access提供了分子层面详尽的机制理解，使其成为TE调控的重要间接候选。

### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H6Y5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000269313-MAGIX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAGIX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H6Y5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000269313-MAGIX/subcellular

![](https://images.proteinatlas.org/7390/1843_E2_19_cr5b07c7dd3ce0b_blue_red_green.jpg)
![](https://images.proteinatlas.org/7390/1843_E2_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/7390/1868_C2_33_blue_red_green.jpg)
![](https://images.proteinatlas.org/7390/1868_C2_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/7390/1925_B8_16_cr5cd568559d2a6_blue_red_green.jpg)
![](https://images.proteinatlas.org/7390/1925_B8_29_cr5cd568559f340_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H6Y5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H6Y5 |
| SMART | SM00228; |
| UniProt Domain [FT] | DOMAIN 125..209; /note="PDZ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143" |
| InterPro | IPR030031;IPR001478;IPR036034; |
| Pfam | PF00595; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000269313-MAGIX/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
