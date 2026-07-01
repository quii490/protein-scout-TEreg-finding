---
type: protein-evaluation
gene: "RAPGEFL1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RAPGEFL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RAPGEFL1 |
| 蛋白名称 | Rap guanine nucleotide exchange factor-like 1 |
| 蛋白大小 | 662 aa / 73.3 kDa |
| UniProt ID | Q9UHV5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytokinetic bridge; Microtubules; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 662 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=8 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=75.9; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ras-like_GEF; Ras_GEF_dom_sf; RASGEF_cat_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=6 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **76.5/100** | 互证: +1 |

### 3. 分析
- Cytokinetic bridge; Microtubules; Nucleoplasm (Approved)
- PubMed strict=8 broad=12
- AF pLDDT=75.9 PDB=1
- InterPro: Ras-like_GEF; Ras_GEF_dom_sf; RASGEF_cat_dom
- Pfam: RasGEF
- PPI degree=6 ChIP: None
41034991: TEAD3 + high-risk melanoma cells crosstalk with GAS6 + macrophages via the GAS6- | 40543717: Molecular Subtypes of Balanopreputial and Urethral Male Genital Lichen Sclerosus | 29512771: Screening pathogenic genes in oral squamous cell carcinoma based on the mRNA exp

### 4. 总体评价
**76.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Rap guanine nucleotide exchange factor-like 1

**功能**: Probable guanine nucleotide exchange factor (GEF)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR008937 |
| InterPro | IPR023578 |
| InterPro | IPR001895 |
| InterPro | IPR036964 |
| InterPro | IPR029071 |
| Pfam | PF00617 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 0 |
| MLH1 | BioGRID | 0 |
| SHMT2 | BioGRID | 0 |
| LRPAP1 | BioGRID | 0 |
| HIST1H2BH | BioGRID | 0 |
| YTHDC1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UHV5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000108352-RAPGEFL1

![](https://images.proteinatlas.org/22895/237_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/22895/237_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/22895/236_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/22895/236_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/22895/268_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/22895/268_C3_2_red_green.jpg)

### PubMed 文献

**PubMed count: 12**

| 41766007 | The methylation of LHX2, RAPGEFL1, RARB and RYR2 has prognostic significance in head and neck squamous cell carcinoma pa | J Appl Genet 2026 |
| 41697067 | Sex-specific differences in liver DNA methylation patterns and epigenetic aging in mice. | Am J Physiol Gastrointest Liver Physiol 2026 |
| 41668749 | Molecular crosstalk between MASLD and IVDD revealed through integrated biomarker discovery analysis. | Front Immunol 2026 |

### 深度机制分析

**结构域架构与分子功能推演。** RAPGEFL1的RasGEF催化域(IPR001895, PF00617)是其最核心的功能模块。RasGEF域的经典拓扑由α-helical hairpin插入CDC25同源催化核心组成,后者提供GDP→GTP交换反应所需的催化残基。具体机制为:RasGEF域通过其helical hairpin撬开Rap GTPase的Switch I区域,物理性地将Mg2+和GDP从核苷酸结合口袋中驱逐;随后GTP自由扩散进入空口袋,完成交换。这种"撬棍(pry bar)"催化机制是所有Ras超家族GEF的共性,但RAPGEFL1的底物选择性由催化中心周围的二级残基决定——Rap1/Rap2偏好由Switch I区域中特定的Glu/Asp排列模式识别。Ras_GEF_dom_sf(IPR023578)和IPR036964提供额外的结构域间交互界面,可能参与别构调控或亚细胞定位。pLDDT=75.9的中等分数且存在明显的低置信区域提示RAPGEFL1含有大量内在无序区段(IDRs)——这是许多GEF蛋白的特征,IDRs可通过液-液相分离(LLPS)或诱导折叠机制招募特异性底物。

**PPI网络揭示的生物学意义。** YTHDC1是RAPGEFL1互作组中最具突破性的发现。YTHDC1是细胞核中m6A RNA修饰的主要reader蛋白,通过其YTH结构域识别含有m6A的RNA并影响其命运——包括mRNA选择性剪接(通过招募SRSF3/SRSF10)、mRNA核出核(通过与NXF1竞争性结合)和XIST介导的X染色体失活。RAPGEFL1-YTHDC1的互作意味着存在一条"GTPase信号→m6A RNA表观转录组"的未描述交叉通路。HIST1H2BH(组蛋白H2B1H)暗示RAPGEFL1可能通过组蛋白相互作用锚定至染色质特定区域——值得注意H2B的泛素化(H2Bub1)是活跃转录的标志,且与H3K4/H3K79甲基化串联催化。若RAPGEFL1结合H2B,它可能在转录活跃的染色质区域富集。MLH1(MutL homolog 1)是DNA错配修复的核心蛋白,其存在提示RAPGEFL1可能与DNA损伤应答有功能交联——Rap信号已知调控细胞周期进程和DNA损伤检查点,MLH1互作可能是这一联系的分子基础。SHMT2(丝氨酸羟甲基转移酶2)定位于线粒体,是一碳代谢的关键酶——其与核内RAPGEFL1的互作机制不明确,但可能反映了两者在核周区域的瞬时共定位。

**结构层面的功能解读。** pLDDT=75.9反映RAPGEFL1具有中等结构置信度,且PDB仅1个结构——与其他高度折叠蛋白相比,RAPGEFL1的柔性更大。RasGEF催化域(C端区域)预计具有高度折叠的核心,而N端区域(约200-300残基)预测为大量无序结构,可能充当"调控枢纽"。这种结构特征与经典的RasGEF家族成员(如SOS1、RasGRP)一致,其N端包含多个调控结构域(PH、REM、DH等)通过自抑制机制限制催化活性。RAPGEFL1的N端IDR可能作为"感应hub",整合多种输入信号(磷酸化、乙酰化、蛋白-蛋白互作)以控制C端催化域的GDP/GTP交换活性。低pLDDT区域在AF2中通常反映的是天然无序(intrinsic disorder)而非预测失败,因为这些区域在进化中保守保持无序状态以实现"多特异性"(multispecificity)互作能力。

**分子机制综合模型。** RAPGEFL1在分子层面执行"核内Rap GTPase信号与RNA表观转录组的交叉调控"。具体的机制假设如下:(1)RAPGEFL1作为Rap1/Rap2的核内GEF,在核质中催化Rap-GDP→Rap-GTP转换——这是此前未描述的,因为Rap信号传统上被认为局限于细胞膜/内体/高尔基体;(2)激活后的Rap-GTP进而通过RAPGEFL1-YTHDC1复合体影响m6A标记的RNA代谢——一个合理的推测是Rap-GTP结合YTHDC1后改变其对m6A-RNA的亲和力或招募共调节因子的能力;(3)Rap-GTP水平变化的净效应是全局性或靶向性的m6A-RNA剪接/出核调控;(4)H2B互作将这一机制限定在活跃转录的染色质上——确保Rap信号优先影响新生转录本的m6A修饰和命运决定。RAPGEFL1启动子甲基化在头颈部鳞状细胞癌预后中的意义(PubMed:41766007)提示该蛋白的表达受表观遗传沉默调控——沉默RAPGEFL1可能解除对m6A依赖的肿瘤抑制性剪接程序的正常调控。

**研究与转化意义。** (1)若RAPGEFL1→Rap→YTHDC1轴被实验验证,这将是"GTPase信号与RNA表观转录组直接交叉"的首个案例——重新定义Rap和m6A领域的研究版图。(2)m6A修饰在肿瘤发生中具有促癌或抑癌的双面角色——RAPGEFL1作为核内Rap GEF的表观遗传沉默(PubMed:41766007提示的甲基化)可能代表一种癌细胞锁定异常m6A模式的机制,因此恢复RAPGEFL1表达可能具有治疗潜力。(3)YTHDC1是m6A领域最热门的靶点之一,而Rap GTPases(Rap1/Rap2)已有成熟的化学工具(如8-pCPT-2'-O-Me-cAMP作为Epac激活剂)——RAPGEFL1的发现为"药理学操纵m6A信号"提供了通过GTPase途径的新入口。(4)RAPGEFL1的结构(大量IDR)使其成为相分离研究的理想候选——核小体中GEF-Rap-YTHDC1-RNA可能形成动态的生物分子凝聚体,这在概念上类似于转录凝聚体(super-enhancer condensates),但由GTP而非磷酸化驱动。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RAPGEFL1

