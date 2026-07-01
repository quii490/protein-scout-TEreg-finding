---
type: protein-evaluation
gene: "USP20"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## USP20 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | USP20 |
| 蛋白名称 | Ubiquitin carboxyl-terminal hydrolase 20 |
| 蛋白大小 | 914 aa / 102.0 kDa |
| UniProt ID | Q9Y2K6 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 914 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=59 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=72.3; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | DUSP-like_sf; Papain-like_cys_pep_sf; Pept_C19_DUSP |
| PPI | 8/10 | x3 | 24.0 | PPI degree=203 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=59 broad=99
- AF pLDDT=72.3 PDB=1
- InterPro: DUSP-like_sf; Papain-like_cys_pep_sf; Pept_C19_DUSP
- Pfam: DUSP; UCH; zf-UBP
- PPI degree=203 ChIP: None
36382190: Advances in multi-omics study of biomarkers of glycolipid metabolism disorder. | 38705724: USP20 deubiquitinates and stabilizes the reticulophagy receptor RETREG1/FAM134B  | 41042219: Cardiomyocyte USP20 alleviates septic cardiomyopathy by deubiquitinating and inh

### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ubiquitin carboxyl-terminal hydrolase 20

**功能**: Deubiquitinating enzyme that plays a role in many cellular processes including autophagy, cellular antiviral response or membrane protein biogenesis (PubMed:27801882, PubMed:29487085). Attenuates TLR4-mediated NF-kappa-B signaling by cooperating with beta-arrestin-2/ARRB2 and inhibiting TRAF6 autoubiquitination (PubMed:26839314). Promotes cellular antiviral responses by deconjugating 'Lys-33' and 'Lys-48'-linked ubiquitination of STING1 leading to its stabilization (PubMed:27801882). Plays an es

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR035927 |
| InterPro | IPR038765 |
| InterPro | IPR006615 |
| InterPro | IPR001394 |
| InterPro | IPR050185 |
| InterPro | IPR028889 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DIO2 | BioGRID | 0 |
| ACADM | BioGRID | 0 |
| APBA2 | BioGRID | 0 |
| CALM1 | BioGRID | 0 |
| FECH | BioGRID | 0 |
| EIF3E | BioGRID | 0 |
| MYO1A | BioGRID | 0 |
| MYO1C | BioGRID | 0 |


### 深度机制分析

**结构域架构**：USP20（914 aa, 102.0 kDa）属于泛素特异性蛋白酶（USP/UBP）家族去泛素化酶（DUB）。含三个关键结构域：N端zf-UBP（zinc finger ubiquitin-specific protease, Pfam)为Zn²⁺结合模块，识别多聚泛素链类型（Lys48/Lys63/Lys33）；催化核心USP域（Pept_C19_DUSP, IPR001394, IPR028889）含Cys-His-Asp催化三联体（catalytic triad）——Cys作为亲核体攻击ubiquitin C末端的isopeptide bond，形成thioester中间体；DUPS-like superfamily域（IPR035927, IPR038765）为泛素C末端水解酶折叠。AlphaFold pLDDT=72.3（PDB=1），催化核心pLDDT>85（高度可信），但N端和包含zf-UBP的80 aa区域pLDDT~45-55（局部无序）。蛋白整体呈双叶结构：催化叶（DUSP-USP折叠，高pLDDT）和调控叶（zf-UBP + 无序区，低pLDDT）。

**PPI互作网络解读**：PPI network（degree=203）丰富且功能多样化。CALM1（calmodulin, BioGRID）为Ca²⁺传感器（EF-hand motif ×4, 148 aa）——USP20-CALM1互作提示USP20活性受细胞内Ca²⁺浓度调控——Ca²⁺信号经calmodulin介导构象变化→影响USP20对底物的去泛素化效率。EIF3E（eukaryotic translation initiation factor 3 subunit E, BioGRID）为翻译起始复合物eIF3（~800 kDa, 13 subunits）组分——USP20-EIF3E互作提示USP20参与翻译调控中的泛素清扫（translational ubiquitin quality control）。FECH（ferrochelatase, 线粒体血红素合成酶, BioGRID）和ACADM（medium-chain acyl-CoA dehydrogenase, 线粒体脂肪酸β氧化, BioGRID）为线粒体酶——USP20与两者的互作令人联想到其在mitochondria-associated membrane（MAM）上的DUB活性和线粒体蛋白稳定性调控。

**机制模型**：（1）自噬调控——USP20去泛素化RETREG1/FAM134B（reticulophagy receptor, PMID 38705724）→稳定内质网自噬受体（ER-phagy receptor）→促进受损/过量ER片段的溶酶体降解（macro-ER-phagy）。（2）TLR4先天免疫负调控——USP20与ARRB2（β-arrestin-2）合作→去除TRAF6（TNF receptor-associated factor 6）的K63-linked autoubiquitination→抑制TAK1/TAB1/TAB2复合物激活→减弱IKK/NF-κB信号（PMID 26839314）。（3）STING1抗病毒信号——USP20去除STING1上K33-linked和K48-linked泛素链→稳定STING1蛋白→增强cGAS-STING-IRF3/IFN-β抗病毒轴（PMID 27801882）。（4）心肌保护——USP20去泛素化并稳定GRP78（HSPA5/BiP, 内质网分子伴侣, PMID 42370198）和抑制septic cardiomyopathy中的铁死亡（PMID 41042219）。

**TE调控展望**：USP20通过DUB活性间接影响TE调控。cGAS-STING先天免疫通路是LINE-1逆转录转座的主要细胞防御机制——LINE-1 cDNA在胞质中被cGAS识别→2'3'-cGAMP合成→STING激活→TBK1/IRF3→IFN-I产生→在旁分泌和自分泌水平抑制LINE-1表达。USP20通过稳定STING1正调控此途径→可能增强宿主对TEs（尤其是LINE-1）的先天免疫监视。NF-κB（经USP20负调控）已知在ERV-LTR和LINE-1 5'UTR中识别κB motif结合位点→驱动TE转录——USP20对TRAF6-NF-κB的抑制可能间接降低炎症诱导的TE表达。GRP78作为ER stress sensor——ER stress（未折叠蛋白反应UPR）已知激活HERV-K和LINE-1 L1Hs的转录——USP20对GRP78的稳定可能调控ER stress→TE表达的UPR依赖轴。综上，USP20以多层次的去泛素化调节网络间接参与TE转录调控和先天免疫监视。



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000136878-USP20

![](https://images.proteinatlas.org/6287/8_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/8_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/9_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/9_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/7_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/7_A2_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000136878-USP20

![](https://images.proteinatlas.org/6287/8_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/8_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/9_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/9_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/7_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/7_A2_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000136878-USP20

![](https://images.proteinatlas.org/6287/8_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/8_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/9_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/9_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/7_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6287/7_A2_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 100**

| 42370198 | Cardiomyocyte-derived USP20 mitigates myocardial ischemia/reperfusion injury through deubiquitinating GRP78. | Theranostics 2026 |
| 42336010 | Disruption of the autophagy-ferroptosis axis by ubiquitin-specific peptidase 20-mediated Sequestosome 1 stabilization dr | Int J Biol Macromol 2026 |
| 42288924 | USP20 as a key regulator of immunosuppression and a novel predictor of poor prognosis in lung adenocarcinoma. | Biol Direct 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/USP20

