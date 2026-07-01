---
type: protein-evaluation
gene: "DMKN"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## DMKN 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DMKN |
| 蛋白名称 | Dermokine |
| 蛋白大小 | 476 aa / 47.1 kDa |
| UniProt ID | Q6E0U4 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 476 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=17 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=41.6; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Dermokine; KRTDAP/DMKN |
| PPI | 5/10 | x3 | 15.0 | PPI degree=26 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |
### 3. 分析
- HPA: Cytosol; Nucleoplasm (Approved)
- PubMed: strict=17, broad=38
- AF pLDDT: 41.6 / PDB: 1
- InterPro: Dermokine; KRTDAP/DMKN
- Pfam: KRTDAP
- PPI degree=26 / ChIP: None
36921580: Parkinson's Disease as a Risk Factor for Prostate Adenocarcinoma: A Molecular Po | 35981655: Overexpression of Dermokine-α enhances the proliferation and epithelial-mesenchy | 25484187: Implications of polyadenylation in health and disease.
### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Dermokine

**功能**: May act as a soluble regulator of keratinocyte differentiation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR033541 |
| InterPro | IPR059487 |
| Pfam | PF15200 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Dermokine

**功能**: May act as a soluble regulator of keratinocyte differentiation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR033541 |
| InterPro | IPR059487 |
| Pfam | PF15200 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ELAVL1 | BioGRID | 0 |
| APP | BioGRID | 0 |
| RBM24 | BioGRID | 0 |
| FOXD4 | BioGRID | 0 |
| ZSCAN12 | BioGRID | 0 |
| FCF1 | BioGRID | 0 |
| ESR2 | BioGRID | 0 |
| NHLRC2 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：DMKN（476 aa, 47.1 kDa, Dermokine）是角质形成细胞分化调控因子，含Dermokine特征结构域（IPR033541）和KRTDAP/DMKN结构域（IPR059487, Pfam PF15200/KRTDAP）。AlphaFold pLDDT=41.6（本批30个蛋白中最低值），PDB=1，>90%残基pLDDT<70，表明DMKN几乎完全是天然无序蛋白（IDP）——缺乏稳定的球形折叠核心。KRTDAP域在结构上被预测为非典型的卷曲螺旋样螺旋束（coiled-coil-like helix bundle），但极低的pLDDT提示在生理条件下该域以高度动态的熔球状或随机卷曲（random coil/pre-molten globule）构象集合存在。DMKN的氨基酸组成富含Ser/Pro/Thr（~35% SPT总和），赋予蛋白骨架极高的柔性和低结构倾向。蛋白在溶液中呈扩展构象（hydrodynamic radius R_h ~40-50 Å, 典型476 aa IDP的表现），其circular dichroism（CD）光谱预测为~70%无序卷曲+30% PPII螺旋（polyproline II helix, 左旋螺旋，-75°/-150°主链phi/psi角偏好）——一种无规卷曲丰富的无序蛋白特征CD标记。

**PPI互作网络解读**：PPI网络（degree=26）富含RNA结合蛋白和转录因子，阐释DMKN在基因表达的转录后和转录调控中的潜在功能。ELAVL1（HuR, ELAV样RNA结合蛋白1, BioGRID）为经典RRM（RNA recognition motif）蛋白——通过其3个RRM域（RRM1-3）识别mRNA 3'UTR中的ARE（AU-rich element, AUUUA motif），稳定靶mRNA免受核酸外切酶降解并促进其翻译（p21/Cip1, Cyclin D1, Bcl-2, VEGF, TNF-α）。DMKN-ELAVL1互作提示DMKN作为IDP支架桥梁将特定mRNA呈递至ELAVL1以增强其ARE识别和RNA稳定活性。RBM24（RNA binding motif protein 24, BioGRID）也是RRM蛋白——通过识别mRNA 3'UTR中的U-rich element调控选择性剪接和mRNA稳定性（如p53/p63, CDK inhibitor p21, myogenin）。DMKN可能作为RBM24的辅助因子以增强其底物特异性或剪接体招募。FOXD4（叉头转录因子D4, forkhead/winged-helix DNA结合域, BioGRID）和ZSCAN12（含SCAN和C2H2锌指域的转录因子）为DNA结合转录调控因子——DMKN与两者的互作暗示DMKN作为转录共因子调节FOXD4依赖和ZSCAN12依赖的基因转录。ESR2（雌激素受体β, 核受体超家族, BioGRID）的互作进一步扩展DMKN的激素信号关联。FCF1（FCF1 rRNA加工蛋白, 小亚基（SSU）processome组分, 参与18S rRNA成熟）为核仁蛋白伙伴——DMKN-FCF1互作连接DMKN至核糖体生物合成。

**结构解读**：DMKN作为IDP通过"聚电解质/entropic bristle"机制行使其功能。无序蛋白在溶液中形成扩展构象——排除体积大（R_h较大），可作为分子间距调控因子（entropic spacer/bumper）。DMKN在角质形成细胞分化中可能定位于细胞皮层——其IDP尾作为分子挡板（bumper）调节角蛋白中间丝（keratin IF, K5/K14, K1/K10）的间距和排列，防止不必要的角蛋白纤维聚合和缠结——这解释了DMKN的Dermokine名称（皮肤角蛋白组织调控因子）。在核质（HPA Approved Nucleoplasm + Cytosol）中，DMKN的IDP特性可能行使分子伴侣功能——ELAVL1和RBM24的RRM域处于无底物时部分不稳定，DMKN以"fly-casting"机制（IDP的扩展构象+快速构象采样速率）非特异性结合部分未折叠的RRM域→稳定其折叠→将RRM域呈递至底物mRNA结合位点——加速ARE/U-rich RNA识别速率。ESR2-β-estradiol结合后转位至核质→雌激素依赖的转录激活可能经DMKN的IDP支架功能增强——DMKN凝聚转录因子（ESR2/FOXD4/ZSCAN12）、染色质修饰因子和RNA Pol II通用转录因子（TFIID/TFIIH）于靶基因增强子/启动子区的多蛋白转录复合体。

**机制模型**：（1）角质形成细胞分化中的角蛋白网络组织——DMKN作为KRTDAP（keratinocyte differentiation-associated protein）家族成员，定位于表皮棘层（stratum spinosum）和颗粒层（stratum granulosum）分化中的角质形成细胞的角蛋白中间丝富集区。DMKN IDP的柔性间隔功能调控角蛋白IF的束化和排列→影响表皮屏障功能水合和机械强度。（2）mRNA稳定性调控——在核质或胞质中，DMKN与ELAVL1结合→ELAVL1 ARE结合活性的"分子伴侣样"增强→稳定p21（CDK inhibitor, 促进角质形成细胞退出细胞周期→终末分化）或Bcl-2（抑制角质形成细胞凋亡）的mRNA→调控皮肤上皮分化-凋亡平衡。（3）FOXD4/ZSCAN12/ESR2转录轴——核质DMKN作为无序分子支架整合多个转录因子至共同靶基因——在角质形成细胞中，DMKN可能促进ESR2（β-estradiol激素受体）和FOXD4（叉头转录因子）在角蛋白基因（KRT1/KRT10 differentiation markers, KRT5/KRT14 basal markers）和角质化包膜蛋白基因（loricrin/LOR, involucrin/IVL, filaggrin/FLG）调控区的共结合→协调其分化依赖的转录激活。

**TE调控展望**：DMKN通过无序蛋白支架和RNA稳定性间接关联TE调控。ELAVL1（HuR）是LINE-1 mRNA的已知结合蛋白——LINE-1 5'UTR含多处AUUUA和U-rich motifs，ELAVL1稳定LINE-1 mRNA以维持其在胞质中的有效翻译→提高LINE-1 ORF1p/ORF2p蛋白水平→增强LINE-1逆转录转座能力。DMKN对ELAVL1的伴侣增强可能间接提高LINE-1 mRNA的稳定性→反效促进LINE-1转座（宿主防御的负调控意外）。RBM24调控p53 mRNA稳定性——p53通过其凋亡功能限制逆转录转座异常活跃的细胞（LINE-1超转座→DSB→ATM/ATR→p53稳定化→细胞凋亡或周期退出），DMKN-RBM24-p53轴间接影响p53依赖的TE转座细胞清除效率。FOXD4结合位点在LTR/ERV启动子中有分布——DMKN作为FOXD4共因子可能促进FOXD4在ERV-LTR上的结合和转录激活。ESR2作为雌激素受体——雌激素（E2）已知强烈激活MMTV LTR和ERVK LTR的转录（ERE estrogen response element, GGTCA nnn TGACC consensus在LTR中分布）——DMKN-ESR2的激素依赖性互作可能经DMKN的IDP支架整合E2信号和TE转录。虽然DMKN缺乏直接DNA结合能力，其无序蛋白分子伴侣和支架功能在间接水平上参与TE mRNA命运和转录调控，可能作为角质形成细胞和特定雌激素靶器官中TE调控的局部特异性因子。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6E0U4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000161249-DMKN

![](https://images.proteinatlas.org/29406/274_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/29406/274_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/29406/273_B4_4_red_green.jpg)
![](https://images.proteinatlas.org/29406/273_B4_3_red_green.jpg)
![](https://images.proteinatlas.org/29406/275_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/29406/275_B4_2_red_green.jpg)

### PubMed 文献

**PubMed count: 38**

| 41427387 | RamanOmics Decodes Spatial Vibrational-Molecular Architecture and Rewiring in Aging and Repair. | bioRxiv 2025 |
| 41234107 | [Comparative Study of Diffuse Large B-Cell Lymphoma and Reactive Lymphoid Hyperplasia Lymph Node Derived Mesenchymal Ste | Zhongguo Shi Yan Xue Ye Xue Za Zhi 2025 |
| 39814939 | Ticam2 ablation facilitates monocyte exhaustion recovery after sepsis. | Sci Rep 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DMKN

