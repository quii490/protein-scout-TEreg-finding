---
type: protein-evaluation
gene: "WARS1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## WARS1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | WARS1 |
| 蛋白名称 | Tryptophan--tRNA ligase, cytoplasmic |
| 蛋白大小 | 471 aa / 53.2 kDa |
| UniProt ID | P23381 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 471 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=27 |
| 三维结构 | 10/10 | x3 | 30.0 | pLDDT=91.6; PDB=13 |
| 调控结构域 | 4/10 | x2 | 8.0 | aa-tRNA-synth_I_CS; aa-tRNA-synth_Ic; Rossmann-like_a/b/a_fold |
| PPI | 5/10 | x3 | 15.0 | PPI degree=37 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=27 broad=68
- AF pLDDT=91.6 PDB=13
- InterPro: aa-tRNA-synth_I_CS; aa-tRNA-synth_Ic; Rossmann-like_a/b/a_fold
- Pfam: tRNA-synt_1b; WHEP-TRS
- PPI degree=37 ChIP: None
35264796: Tryptophan depletion results in tryptophan-to-phenylalanine substitutants. | 39408566: Pinpointing Novel Plasma and Brain Proteins for Common Ocular Diseases: A Compre | 39515413: Wars1 downregulation in hepatocytes induces mitochondrial stress and disrupts me

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Tryptophan--tRNA ligase, cytoplasmic

**功能**: Catalyzes the attachment of tryptophan to tRNA(Trp) in a two-step reaction: tryptophan is first activated by ATP to form Trp-AMP and then transferred to the acceptor end of the tRNA(Trp)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001412 |
| InterPro | IPR002305 |
| InterPro | IPR014729 |
| InterPro | IPR002306 |
| InterPro | IPR009068 |
| InterPro | IPR000738 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：WARS1（471 aa, 53.2 kDa, P23381, Tryptophan--tRNA ligase, cytoplasmic）是I类氨酰tRNA合成酶（aaRS）家族成员，催化Trp-tRNA(Trp)的合成。含三个功能模块：（1）Rossmann-fold催化域（IPR001412, 含HIGH和KMSKS保守motif）——经典的beta-alpha-beta Rossmann核苷酸结合折叠，ATP和Trp在此区域被激活形成Trp-AMP混合酸酐；（2）WHEP-TRS域（Pfam WHEP-TRS）——独特的helix-turn-helix结构域，在I类aaRS中参与非经典功能，如血管新生信号中的VE-cadherin结合；（3）C末端反密码子结合域（IPR002306）——识别tRNA(Trp)的CCA反密码子stem-loop。AlphaFold pLDDT=91.6是最高值之一，PDB=13个实验结构，结构可信度极高。

**PPI互作网络解读**：PPI degree=37，高度富集aaRS家族成员——AARS1（AlaRS, STRING 881）、MARS1（MetRS, STRING 878）、KARS1（LysRS, STRING 868）、VARS1（ValRS, STRING 846）、LARS1（LeuRS, STRING 844）、HARS1（HisRS, STRING 848）等全部胞质I类aaRS构成密集互作网络——这些aaRS在胞质中形成多tRNA合成酶复合体（multi-tRNA synthetase complex, MSC）——与MSC scaffold蛋白（AIMP1/p43, AIMP2/p38, AIMP3/p18）非共价组装成~1.2 MDa超分子机器。WARS2（线粒体TrpRS, STRING 829）互作连接胞质和线粒体tRNA氨酰化体系。

**结构解读**：pLDDT=91.6和13个PDB结构提供了WARS1催化机制的原子级分辨率。Trp-AMP合成遵循two-step机制：（1）Trp + ATP → Trp-AMP + PPi（腺苷化）；（2）Trp-AMP + tRNA(Trp) → Trp-tRNA(Trp) + AMP（tRNA charging）。Trp吲哚侧链堆叠在Phe/Tyr保守残基的芳香笼中，ATP adenine与Asp/Glu残基形成氢键。WHEP-TRS域在血管新生信号中经proteolytic cleavage释放为mini-TrpRS——获得胞外细胞因子活性——结合VE-cadherin胞外域抑制VEGF诱导的血管通透性。

**机制模型**：（1）经典功能——胞质Trp-tRNA(Trp)合成——WARS1作为MSC组分催化Trp激活和tRNA(Trp)氨酰化——确保Trp密码子（UGG）在核糖体A位被正确解码。（2）非经典功能——N端截短体（mini-TrpRS/T2-TrpRS）胞外分泌后作为促炎/抗血管新生信号分子，激活巨噬细胞和中性粒细胞（通过TLR4-MyD88和TLR2-MyD88 pathway）。（3）Trp depletion/stress response（PMID:35264796）——细胞Trp不足时Trp codon核糖体暂停→ribosome-associated quality control→GCN2/ISR激活→全局翻译抑制——WARS1作为Trp sensor间接参与氨基酸应激信号。（4）肝细胞线粒体应激（PMID:39515413）——WARS1下调导致线粒体应激和代谢紊乱。

**TE调控展望**：WARS1 TE调控关联为间接路径。Trp作为最稀有的氨基酸（仅1个UGG codon），其tRNA charging效率直接影响TE编码蛋白（LINE-1 ORF1p/ORF2p, ERV Gag/Pol/Env）的翻译延伸速率。WARS1下调导致Trp-tRNA(Trp)不足→核糖体在TE mRNA的UGG codon上暂停→ribosome collision→RQC-mediated mRNA decay→TE mRNA周转加速——这构成翻译水平的TE表达调控——与转录水平的TRIM28/KRAB-ZNF/KAP1沉默协同限制TE蛋白产量。


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000140105-WARS1

![](https://images.proteinatlas.org/18944/116_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/116_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/115_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/115_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/117_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/117_E8_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000140105-WARS1

![](https://images.proteinatlas.org/18944/116_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/116_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/115_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/115_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/117_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/117_E8_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000140105-WARS1

![](https://images.proteinatlas.org/18944/116_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/116_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/115_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/115_E8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/117_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18944/117_E8_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 68**


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/WARS1

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| WARS2 | STRING | 829 |
| AARS1 | STRING | 881 |
| MARS1 | STRING | 878 |
| MARS2 | STRING | 824 |
| QARS1 | STRING | 835 |
| YARS2 | STRING | 851 |
| KARS1 | STRING | 868 |
| WARS1 | STRING | 862 |
| SARS1 | STRING | 853 |
| PARS2 | STRING | 835 |
| YARS1 | STRING | 454 |
| VARS1 | STRING | 846 |
| LARS1 | STRING | 844 |
| HARS1 | STRING | 848 |

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| WARS2 | STRING | 829 |
| AARS1 | STRING | 881 |
| MARS1 | STRING | 878 |
| MARS2 | STRING | 824 |
| QARS1 | STRING | 835 |
| YARS2 | STRING | 851 |
| KARS1 | STRING | 868 |
| WARS1 | STRING | 862 |
| SARS1 | STRING | 853 |
| PARS2 | STRING | 835 |
| YARS1 | STRING | 454 |
| VARS1 | STRING | 846 |
| LARS1 | STRING | 844 |
| HARS1 | STRING | 848 |
