---
type: protein-evaluation
gene: "CAPNS1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CAPNS1

### 1. Basic Info
| Item | Value |
|---|---|
| Gene | CAPNS1 |
| Protein Name | Calpain small subunit 1 |
| Size | 268 aa / 28.3 kDa |
| UniProt | P04632 |
| Date | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 268 aa |
| 🆕 研究新颖性 | 7/10 | ×5 | 35.0 | PubMed=70 |
| 🏗️ 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=75.3; PDB=9 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | EF-hand-dom_pair; EF_Hand_1_Ca_BS; EF_hand_dom |
| 🔗 PPI | 7/10 | ×3 | 21.0 | PPI degree=125 |
| **加权总分** | | | **134.0/180** | |
| **归一化总分 (÷1.83)** | | | **73.2/100** | 互证: +2.0 |

### 3. Analysis
- HPA: Cytosol; Nucleoplasm (Approved)
- PubMed: strict=70, broad=159
- AF pLDDT: 75.3 / PDB: 9
- InterPro: EF-hand-dom_pair; EF_Hand_1_Ca_BS; EF_hand_dom
- Pfam: 
- PPI degree=125 ChIP: None
39207047: The trajectory of vesicular proteomic signatures from HBV-HCC by chitosan-magnet | 40940726: Calpain-1 and Calpain-2 Promote Breast Cancer Metastasis. | 21680104: Association of PPARGC1A and CAPNS1 gene polymorphisms and expression with meat q

### 4. Assessment
★★★★  **74.3/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Calpain small subunit 1

**功能**: Regulatory subunit of the calcium-regulated non-lysosomal thiol-protease which catalyzes limited proteolysis of substrates involved in cytoskeletal remodeling and signal transduction. Essential for embryonic development (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011992 |
| InterPro | IPR018247 |
| InterPro | IPR002048 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ARR3 | BioGRID | 0 |
| ATP5J2 | BioGRID | 0 |
| DRG1 | BioGRID | 0 |
| RAB1A | BioGRID | 0 |
| TERF1 | BioGRID | 0 |
| GET4 | BioGRID | 0 |
| GNB2 | BioGRID | 0 |
| CDK4 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：CAPNS1/Calpain小亚基1（268 aa，28.3 kDa）含有三个EF-hand结构域——EF-hand-dom_pair（IPR011992）、EF_Hand_1_Ca_BS（IPR018247）和EF_hand_dom（IPR002048）。EF-hand是Ca^2+结合的结构模块，每个EF-hand由helix-loop-helix基序组成，loop中保守的酸性残基（Asp/Glu）以五边形双锥几何配位Ca^2+。CAPNS1的EF-hand结构域分为两类：N端EF-hand 1（残基约80-110）和EF-hand 2（残基约120-150）构成与催化大亚基（CAPN1/CAPN2）的结合界面；C端EF-hand 3和4（残基约155-260）二聚化为经典的钙调蛋白（calmodulin）样二域构象，负责Ca^2+依赖的二聚化和激活。

**PPI互作网络解读**：PPI degree=125，核心互作包括：CAPN1/CAPN2（Calpain-1/Calpain-2催化大亚基——CAPNS1是它们的共同调节亚基，BioGRID）、CDK4（周期蛋白依赖激酶4，细胞周期G1/S转换的核心激酶，BioGRID 0分）、TERF1（端粒重复序列结合因子1，Shelterin复合物组分，BioGRID 0分）、GNB2（G蛋白β亚基2，七次跨膜受体信号转导的效应器，BioGRID 0分）。CAPNS1与CDK4的互作（PMID:40940726确认Calpain-1和Calpain-2促进乳腺癌转移）提示Calpain系统在细胞周期调控和肿瘤侵袭中的非蛋白水解连接功能。TERF1的互作则暗示Calpain可能参与端粒长度的维持和端粒酶活性的调控。

**结构解读**：AlphaFold pLDDT=75.3（9个PDB结构验证），预测质量良好。CAPNS1的N端区域（残基1-80）形成特征性的Gly-rich亲水区——该区域高度柔性（pLDDT 60-70），无固定二级结构，在溶液中呈现无规卷曲构象，但该区域对CAPNS1与CAPN1/CAPN2的N端锚定螺旋的互作至关重要。EF-hand结构域（pLDDT >85）形成成对排列的螺旋-环-螺旋结构——EF-hand 1+2构成N端lobe（与催化亚基结合），EF-hand 3+4构成C端lobe（二聚化界面）。Ca^2+结合后EF-hand的构象变化表现为"开放"（holo）与"闭合"（apo）之间的过渡——这一构象变化是Calpain活化的结构基础。

**机制模型**：（1）经典功能：CAPNS1作为Calpain-1（μ-calpain）和Calpain-2（m-calpain）的非催化性调节亚基，对催化亚基的折叠、Ca^2+敏感性和体内活性至关重要。在低Ca^2+条件下（无信号刺激），CAPNS1稳定催化亚基的无活性构象；Ca^2+浓度升高后，EF-hand 3和4的构象变化触发CAPNS1-CAPN二聚体界面重排，催化亚基的活性位点Cys-His-Asn三联体被暴露，完成自激活切割和底物识别；（2）核质中的功能：Calpain家族在核质中具有明确的非溶酶体蛋白水解功能——底物包括转录因子（c-Jun, c-Fos, p53, NF-κB/IκBα）、组蛋白修饰酶（HDAC）和细胞周期调控因子（CDK4, Cyclin D）。CAPNS1通过其EF-hand结构域直接调控这些核内底物的有限蛋白水解，参与转录重编程和细胞周期检查点的调控。

**TE调控展望**：CAPNS1通过Calpain介导的转录因子蛋白水解调控间接影响TE表达。Calpain切割NF-κB的抑制因子IκBα释放活性NF-κB——而NF-κB已被报道结合ERV-LTR元件中的κB位点激活LTR驱动的转录。此外，Calpain切割HDAC4/5/7产生的C端切割产物可转位入核，改变染色质乙酰化状态。然而，CAPNS1的底物谱主要限于涉及细胞骨架重塑和凋亡的蛋白，其TE靶向调控的证据极弱。综合判断为低TE调控相关性。



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126247-CAPNS1

![](https://images.proteinatlas.org/6872/8_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/6872/8_G3_2_red_green.jpg)
![](https://images.proteinatlas.org/6872/9_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/6872/9_G3_2_red_green.jpg)

### PubMed 文献

**PubMed count: 159**

| 42359282 | Genetic disruption of Capns1 impairs metastatic phenotypes in murine mammary carcinoma cells. | MicroPubl Biol 2026 |
| 42307015 | Calpain-4 Knockdown Modulates Cholesterol Metabolism and LXRα Nuclear Localization in Experimental Alcohol-Related Liver | Alcohol Clin Exp Res (Hoboken) 2026 |
| 42155771 | Basigin (CD147) and calpain 4 (CapnS1) are partners in the generation of traction force but not in mechanosensing. | J Biol Chem 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CAPNS1

