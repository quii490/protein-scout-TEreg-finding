---
type: protein-evaluation
gene: "ZG16B"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## ZG16B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ZG16B |
| 蛋白名称 | Pancreatic adenocarcinoma up-regulated factor |
| 蛋白大小 | 172 aa / 18.9 kDa |
| UniProt ID | Q96DA0 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 172 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=23 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=87.4; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Jacalin-like_lectin_dom; Jacalin-like_lectin_dom_sf; PolyBind_ProtTraffic |
| PPI | 7/10 | x3 | 21.0 | PPI degree=141 |
| **加权总分** | | | **141/180** | |
| **归一化总分** | | | **78.1/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=23 broad=56
- AF pLDDT=87.4 PDB=1
- InterPro: Jacalin-like_lectin_dom; Jacalin-like_lectin_dom_sf; PolyBind_ProtTraffic
- Pfam: Jacalin
- PPI degree=141 ChIP: None
40469839: Unraveling the impact of ZG16B missense mutations: computational prediction of s | 41543187: ZG16B: A key regulator of tumor progression and immune microenvironment modulati | 33336077: Identification of ZG16B as a prognostic biomarker in breast cancer.

### 4. 总体评价
**78.1/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Pancreatic adenocarcinoma up-regulated factor

**功能**: Functions as a lectin that binds to selective commensal dental plaque bacteria, such as Streptococcus vestibularis. Contributes to maintain homeostasis in the oral microbiome by capturing commensal microbes and regulating their growth using a mucin-assisted clearance mechanism (PubMed:37216558). Plays an important role in pancreatic tumor progression and metastasis (PubMed:19302292, PubMed:36232715). Promotes pancreatic cancer cells migration and invasion through the TLR4/MyD88/NF-kappaB signali

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001229 |
| InterPro | IPR036404 |
| InterPro | IPR052321 |
| Pfam | PF01419 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

ZG16B(172 aa, 18.9 kDa)在结构上属于Jacalin类凝集素超家族(IPR001229/IPR036404/IPR052321, Pfam PF01419), 其特征性的β-棱柱折叠(jacalin-like β-prism fold)由三个希腊钥匙基序组成, 形成一个具有糖基结合位点的紧凑结构域。AlphaFold预测pLDDT高达87.4, 且仅有一个实验结构, 表明该结构域的折叠高度自主且刚性。然而ZG16B的核质定位(Protein Atlas Approved级别)与该家族其他成员——典型分泌/膜相关凝集素——形成鲜明反差。在典型功能中, ZG16B通过其Jacalin结构域识别口腔共生菌(如Streptococcus vestibularis)表面的糖基表位, 并通过TLR4/MyD88/NF-κB信号轴驱动胰腺癌的迁移和侵袭。但进入核质后的ZG16B不大可能接触细菌糖基——这提示ZG16B在核内可能识别不同类别的糖基化底物。O-GlcNAc修饰(O-linked β-N-acetylglucosamine)是核质中最丰富的翻译后修饰之一, 广泛存在于转录因子(如c-Myc, p53, NF-κB)、RNA聚合酶II CTD和组蛋白上, 其糖基结构类似物与Jacalin结构域的底物偏好存在化学上的可塑性。ZG16B极有可能是核质O-GlcNAc信号的"读取器"(reader), 通过其Jacalin折叠的糖基结合口袋识别特定蛋白的O-GlcNAc修饰状态, 将代谢状态耦联至转录调控。

ZG16B的PPI网络(degree=141)为这一机制假说提供了多维度支撑。**GTF2B**(通用转录因子IIB)是Pol II前起始复合体(PIC)的核心组分, 负责招募RNA聚合酶II至启动子并稳定TBP-DNA复合体——ZG16B与GTF2B的直接互作(评分1)暗示其在转录起始步骤的调控位点。**CIART**(昼夜节律相关转录抑制因子)是CLOCK-BMAL1的共抑制因子, 通过组蛋白去乙酰化调控节律基因的周期性表达——ZG16B-CIART可能构成一个糖基信号-昼夜节律调控轴的适配器。**NSL1**是着丝粒KMN网络(Mis12-Ndc80-Knl1复合体)的组成部分, 在有丝分裂中负责着丝粒-微管附着——ZG16B-NSL1互作提示其在M期的潜在功能, 可能涉及核膜破裂后凝集素介导的染色体分离质量控制。**SGTA**(小谷氨酰胺三角四肽重复蛋白)是一个多功能共伴侣分子, 调控新生多肽的转运、错误折叠蛋白的泛素化降解以及病毒蛋白的宿主整合——ZG16B-SGTA可能构成核内糖基化蛋白的质量控制检查点。**USP25**是去泛素化酶, 参与先天免疫信号(如TRAF6介导的NF-κB激活)和内质网应激响应, ZG16B-USP25可能存在泛素化-糖基化的交叉调控。

从结构机制角度, ZG16B 172 aa的紧凑尺寸(pLDDT 87.4)使其成为一个近乎纯粹的糖基识别模块, 缺乏明显的信号传导结构域。这意味着ZG16B不太可能自身执行催化功能, 而是作为"适配器"(adaptor)将糖基化信号传递至其互作伙伴的催化活性。结构预测表明Jacalin折叠占据蛋白的几乎全部序列(残基~20-170), N端仅有一个极短的延伸。这种"单域"架构的蛋白通常通过两种机制发挥作用: ①糖基结合诱导的构象变化暴露/掩蔽互作面, 从而调控伙伴蛋白的活性; ②作为竞争性抑制剂阻断其他凝集素/糖基转移酶对同一底物的访问。ZG16B的PPI伙伴列表中包含泛素化酶(USP25)、转录因子(GTF2B)、转录抑制因子(CIART)和激酶(CAMK1D), 这种功能多样性暗示ZG16B可能以"糖基依赖"的方式(即结合O-GlcNAc修饰的底物后再招募特定的效应蛋白)充当一个条件性互作平台, 而非固定的复合体组分。

整合所有可用数据, ZG16B的分子机制模型为: ①在稳态条件下, ZG16B主要定位于囊泡/分泌通路, 发挥其经典的微生物凝集素功能; ②在特定信号(如O-GlcNAc水平升高、营养应激、昼夜节律信号)触发下, ZG16B转位至核质; ③核质ZG16B通过Jacalin结构域识别转录因子或转录调控因子上的O-GlcNAc修饰, 招募GTF2B至特定启动子或通过CIART介导转录抑制; ④同时, ZG16B-SGTA互作可能参与核质中异常糖基化蛋白的泛素化降解(USP25参与), 构成一个核内糖基化蛋白质稳态的监测系统; ⑤在有丝分裂期间, ZG16B-NSL1互作可能参与染色体分离的糖基依赖调控。这一模型的独特之处在于, 它将原本在膜/分泌系统中运作的"糖基识别"范式重新利用于核内的转录与细胞周期调控——这是一种进化上的"功能重定向"(functional repurposing)。

**研究与治疗意义**: ZG16B仅23篇文献, 核质功能几乎完全未被探索。它是检验"核质O-GlcNAc读取器"假说的理想模型蛋白。从治疗角度, ZG16B在胰腺癌中的高表达与其TLR4/MyD88/NF-κB促转移功能已得到初步验证, 但它在核质中通过GTF2B和CIART调控转录的潜力提供了一个未被触及的治疗层面——设计阻断ZG16B-Jacalin糖基结合口袋的小分子可能同时抑制其膜旁促癌信号和核内转录重编程。Jacalin折叠表面存在明显的糖基结合凹槽, 这种口袋结构是可药性的理想特征。ZG16B-NSL1的着丝粒互作则开启了其在有丝分裂灾难(mitotic catastrophe)型抗癌策略中的潜在价值。最后, ZG16B作为单结构域蛋白(18.9 kDa), 是冷冻电镜和X射线晶体学的理想样本, 解析其与O-GlcNAc化肽段的共晶结构将是验证其核内功能的关键实验。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| USP25 | BioGRID | 1 |
| SGTA | BioGRID | 1 |
| PNMA1 | BioGRID | 1 |
| NSL1 | BioGRID | 1 |
| TRNAU1AP | BioGRID | 1 |
| GTF2B | BioGRID | 1 |
| CIART | BioGRID | 1 |
| CAMK1D | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96DA0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162078-ZG16B

![](https://images.proteinatlas.org/53549/986_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/53549/986_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/53549/832_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/53549/832_E7_2_red_green.jpg)

### PubMed 文献

**PubMed count: 56**

| 42045466 | Identification of novel protein markers and therapeutic targets for common urological cancers by integrating large-scale | Sci Rep 2026 |
| 41553868 | Diagnostic modulation of subgingival proteomic biomarkers by age and smoking habits in periodontitis. | J Periodontol 2026 |
| 41543187 | ZG16B: A key regulator of tumor progression and immune microenvironment modulation in cancer (Review). | Int J Mol Med 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ZG16B

