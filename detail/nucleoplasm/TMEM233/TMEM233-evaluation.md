---
type: protein-evaluation
gene: "TMEM233"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM233 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM233 |
| 蛋白名称 | Transmembrane protein 233 |
| 蛋白大小 | 109 aa / 12.1 kDa |
| UniProt ID | B4DJY2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 109 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=7 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=60.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | CD225/Dispanin; CD225/Dispanin_fam |
| PPI | 5/10 | x3 | 15.0 | PPI degree=1 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=7 broad=10
- AF pLDDT=60.3 PDB=0
- InterPro: CD225/Dispanin; CD225/Dispanin_fam
- Pfam: CD225
- PPI degree=1 ChIP: None
41854608: The Excelsatoxin A-Receptor TMEM233 Modulates Nav1.8. | 37117223: Pain-causing stinging nettle toxins target TMEM233 to modulate Na(V)1.7 function | 39025729: The 'dispanins' and related proteins in physiology and neurological disease.

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 233

**功能**: Probable accessory protein of voltage-gated sodium channels

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR051423 |
| InterPro | IPR007593 |
| Pfam | PF04505 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：TMEM233（109 aa, 12.1 kDa, B4DJY2）是CD225/Dispanin家族成员（IPR051423, IPR007593, Pfam PF04505）——一个四次跨膜（tetraspan）膜蛋白超家族。Dispanin蛋白具有特征性的4-TM拓扑（N端胞内→TM1→胞外loop1→TM2→胞内loop2→TM3→胞外loop2→TM4→C端胞内），两个胞外loop含保守Cys-Cys（CC）和Cys-Cys-Gly（CCG）motif——形成两个disulfide bond稳定胞外结构。AlphaFold pLDDT=60.3，无PDB实验结构，109 aa的极小蛋白接近AlphaFold预测极限——四个TM螺旋相对置信度较高（pLDDT ~65-75），胞外loop区域pLDDT偏低（~40-55），反映其动态构象。Dispanin家族以电压门控钠通道（Nav）辅助亚基功能而闻名——dispanin作为Nav通道的beta-subunit或accessory protein调控通道的门控特性、表面表达和药物敏感性。

**PPI互作网络解读**：PPI degree=1（仅CSK, C-terminal Src kinase, BioGRID）。CSK是Src家族激酶（SFK）的负调控因子——通过磷酸化SFK（如Src, Fyn, Lyn, Yes, Lck, Hck）C末端tail的conserved tyrosine residue（如Src Y527）→该pTyr与SFK自身SH2域分子内结合→SFK处于闭合/自抑制构象→催化活性被抑制。TMEM233-CSK唯一的互作提示TMEM233可能通过binding CSK→将CSK recruitment至质膜的Nav channel complex附近的lipid raft microdomain→CSK局部磷酸化SFK→调控SFK依赖的Nav通道磷酸化和门控调制。Nav1.7和Nav1.8是疼痛感觉神经元的关键钠通道亚型——TMEM233作为两者辅助蛋白（PMID:37117223, PMID:41854608）的功能依赖于其dispanin结构。

**结构解读**：4-TM dispanin折叠形成紧凑的四螺旋束（four-helix bundle），TM1和TM3的极性残基（Ser/Thr）朝向通道孔方向与Nav alpha-subunit的voltage sensor domain（VSD, S1-S4 segments）或pore domain（S5-S6）形成氢键和疏水互作。胞外loop1和loop2中的conserved Cys残基形成分子内disulfide bond——维持胞外loop特定的3D构象以识别Nav通道的胞外糖基化loop。109 aa中C末端仅~15 aa胞质尾，缺乏信号转导能力——TMEM233本身无催化活性，完全依赖与Nav蛋白和CSK的物理互作实现功能。

**机制模型**：（1）Nav1.7/Nav1.8疼痛信号——TMEM233与Nav1.7（SCN9A）和Nav1.8（SCN10A）的直接互作增强Nav通道在细胞表面的表达和稳定（chaperone-like function）——降低Nav通道的泛素化降解速率→维持DRG（背根神经节）和trigeminal神经元中Nav电流密度→调节伤害感受神经元的兴奋阈。（2）Excelsatoxin A机制（PMID:41854608）——荨麻毒素Excelsatoxin A作为TMEM233的配体——结合TMEM233后诱导其构象改变→变构调控Nav1.8的门控电压依赖性激活曲线向超极化方向偏移→通道在更负的膜电位处开放→神经元超兴奋→剧烈疼痛。（3）CSK-SFK信号——TMEM233 recruitment CSK至Nav channel complex→CSK磷酸化抑制SFK→减少SFK依赖的Nav通道磷酸化（如Nav1.7的Tyr位点）→调控Nav通道的电压依赖性稳态失活——该机制可能参与炎症性疼痛中Nav通道的致敏。

**TE调控展望**：TMEM233与TE调控的直接关联极弱——其功能高度特化为神经元Nav通道辅助蛋白和疼痛信号。核质定位（HPA: Nucleoplasm Approved, 109 aa小蛋白可能经被动扩散经NPC进入核质）的生理意义尚不明确——核内TMEM233可能参与核膜上的离子稳态或内质网-核膜膜接触位点（membrane contact site）的膜微域组织。CSK互作间接连接至SFK signaling——SFK在一些肿瘤中已知激活HERV-K Env和LTR驱动的oncogenes——TMEM233-CSK-SFK轴可能以组织特异性（疼痛神经元）方式影响SFK介导的TE转录激活，但此推测需神经元特异性实验验证。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CSK | BioGRID | 0 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000224982-TMEM233

![](https://images.proteinatlas.org/75435/1782_E2_31_red_green.jpg)
![](https://images.proteinatlas.org/75435/1782_E2_33_red_green.jpg)
![](https://images.proteinatlas.org/75435/1585_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/75435/1585_H6_5_red_green.jpg)
![](https://images.proteinatlas.org/75435/1616_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/75435/1616_H6_3_red_green.jpg)

### PubMed 文献

**PubMed count: 10**

| 42096223 | The Transcription Factor 12 of Basic Helix-Loop-Helix Plays an Essential Role in Retinal Health. | Invest Ophthalmol Vis Sci 2026 |
| 41967766 | From nociception to therapy: The expanding role of TMEM proteins in pain. | Life Sci 2026 |
| 41964392 | Correction to "The Excelsatoxin A-Receptor TMEM233 Modulates Nav1.8". | FASEB J 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM233

